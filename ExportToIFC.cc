/**
 * Copyright (c) 2012-2013 Insieme Networks. All rights reserved.
 *
 *  $Id$
 *
 * ExportToIFC.cc
 */

/* 
 * CSCuq76985: stat() hits EOVERFLOW on 32bit systems if the file's size exceeds (2<<31)-1 bits.
 * Override by setting _FILE_OFFSET_BITS 64
 * This needs to be declared before including other header files.
 */
#define _FILE_OFFSET_BITS 64

#include <stdlib.h>
#include <boost/filesystem.hpp>
#include <boost/algorithm/string.hpp>
#include <vector>

#include <dataexport/ExportToIFC.h>
#include <dataexport/ExportUtils.h>
#include <dataexport/DbgrExportUtils.h>
#include <corefiles/CoreUtils.h>

#include "core/log/LogConfig.h"
#include "core/log/Log.h"
#include "core/utils/String.h"
#include "mo/dbgexp/TechSupPMo.h"
#include "mo/dbgexp/CorePMo.h"
#include "mo/dbgexp/TechSupOnDMo.h"

#include "dbgr/src/gen/ifc/app/Svc.h"

#include "core/otracker/OTracker.h"

#ifdef DME_NXOS 
#include <isan/sysmgr_intf.h>  
#endif

#define SSH_KNOWN_HOSTS_OPT "UserKnownHostsFile=/dev/null"
#define SSH_HOSTKEY_CHECK_OPT "StrictHostKeyChecking=no"

#define PROTOCOL_RSYNC_STR "rsync"

#define ERROR_BUFFER_LEN 1024
#define MAX_RETRY_COUNT 1

#define LOG_NAMESPACE ifc_dbgr
#define RETRY_TIMEOUT_SEC 30


namespace dbgexp
{

    ExportToIFC::ExportToIFC()
    {
        aStatusUri = "";
        aStatusDbUri = "";
        aStatusLogsUri = "";
        aConfigSize = 0;
        aDbSize = 0;
        aLogsSize = 0;
        aStatus = dbgexp::CONST_EXPORT_STATUS_PENDING;
        aStatusStr = "Triggered export, pending collection";
        aDataType = dbgexp::CONST_DATA_TYPE_TECH_SUPPORT;
        lTmpFiles = {};
        OTRACKER_CONSTRUCTOR();
    }


    void ExportToIFC::
    getDestIFC(frmwrk_addrss::Appliance::Id& aInOutAppId, base::Ip& aInOutDestIp)
    {
        aInOutAppId = -1;
        bool isPlatformIfc = proc::Svc::isPlatformIfc();
        aInOutDestIp = ExportUtils::getIFCIp(isPlatformIfc, aInOutAppId);
    }

    
    void ExportToIFC::
    formatExportDestUri(const frmwrk_addrss::Appliance::Id aInAppId, 
                        const base::String& aInFilename, base::String& aInOutExportDestUri)
    {
        aInOutExportDestUri.append("files/");
        aInOutExportDestUri.append(aInAppId);
        aInOutExportDestUri.append("/");

        std::string remotePath = std::string(aInFilename.getBuffer());
        std::size_t position = remotePath.find("techsupport");
        if(position != std::string::npos) {
            aInOutExportDestUri.append((remotePath.substr(position)).c_str());
        }
    }


    bool ExportToIFC::
    constructFilenames(mo::Dn& aInPolicyDn,
            uint64_t aInWindowStartMs,
            frmwrk_addrss::Appliance::Id aInApplId, 
            const base::String& aInSuffix, 
            const base::String& aInCompressionSrcFile, 
            base::String& aInOutCompressedFileNameOnly,
            base::String& aInOutCompressedFile,
            base::String& aInOutRemoteDestFile,
            base::String& aInOutDownloadUri)
    {
        // Format file name aInOutCompressedFile eg. leaf0_sysid-17_<timestamp>.tar.gz
        // Remote file name= dbgexp_<policy-rn>_leaf0_sysid-17_<timestamp>.tar.gz
        base::String lPath;
        if(aDataType == dbgexp::CONST_DATA_TYPE_TECH_SUPPORT)
        {
            DbgrExportUtils::getTechSupFilenames(aInWindowStartMs, lPath,
                file::CONST_TRANSFER_PROTOCOL_SCP,  
                aInPolicyDn.getLastRn().toString(), aInSuffix, 
                aInOutCompressedFile, aInOutRemoteDestFile, aInOutCompressedFileNameOnly);
        }
        else if(aDataType == dbgexp::CONST_DATA_TYPE_CORES)
        {
            DbgrExportUtils::getCoreFilenames(aInWindowStartMs, lPath, 
                aInCompressionSrcFile, file::CONST_TRANSFER_PROTOCOL_SCP,  
                aInPolicyDn.getLastRn().toString(), 
                aInOutRemoteDestFile, aInOutCompressedFileNameOnly);
            aInOutCompressedFile = aInCompressionSrcFile;
        }
        base::String lRemoteFilename = aInOutRemoteDestFile;
        aInOutRemoteDestFile.clear();
        aInOutRemoteDestFile.append(base::SvcConfigParams::getInstance()->getTechSupDirectory());
        aInOutRemoteDestFile.append("/dbgexp_");
        aInOutRemoteDestFile.append(lRemoteFilename);
        
        formatExportDestUri(aInApplId, aInOutRemoteDestFile, aInOutDownloadUri);
        return true;
    }


    void ExportToIFC::
    addToCleanup(base::String aInFileName)
    {
        if(!aInFileName.isEmpty())
        {
            lTmpFiles.insert(aInFileName);
        }
    }


    void ExportToIFC::
    interimCleanup(const base::String& aInFileName, bool aInDeleteDir=true)
    {
        std::set<base::String> lFiles;
        lFiles.insert(aInFileName);
        try {
             removeTempFiles(lFiles, aInDeleteDir);
        } catch (...) {
            LOG_STR(dataexport, none, LOG_DEBUG4) << "Exception: Removing file " << aInFileName;
           return;
       }
    }


    void ExportToIFC::
    removeTempFiles(const std::set<base::String>& aInTmpFiles, bool aInDeleteDir=true) 
    {
        std::set<base::String>::iterator iter;

        for(iter=aInTmpFiles.begin(); iter != aInTmpFiles.end(); iter++)
        {
            LOG_STR(dataexport, none, LOG_DEBUG4) << "Removing file " << *iter; 
            struct stat cfile_info;
            if(!stat((*iter).getBuffer(), &cfile_info))
            {
                if(S_ISDIR(cfile_info.st_mode))
                {
                    if(aInDeleteDir) {
                        boost::filesystem::remove_all((*iter).getBuffer());
                    }
                    else {
                        std::string dirname = (*iter).getBuffer();
                        LOG_STR(dataexport, none, LOG_DEBUG4) << "Removing contents of " << dirname; 
                        boost::filesystem::path dirpath(dirname);
                        for(boost::filesystem::directory_iterator itr(dirpath); 
                            itr!=boost::filesystem::directory_iterator(); ++itr) {
                            if(remove(itr->path()) != 0) {
                                LOG_STR(dataexport, none, LOG_WARN) << "Failed to remove " << itr->path();
                            }
                        }
                    
                    }
                }
                else
                {
                    if(remove((*iter).getBuffer()) != 0) {
                        LOG_STR(dataexport, none, LOG_WARN) << "Failed to remove " << ((*iter).getBuffer());
                    }
                }
            }
        }
    }

    void ExportToIFC::
    cleanup()
    {
        // remove temp files
        if(aDataType == dbgexp::CONST_DATA_TYPE_TECH_SUPPORT)
        {
            removeTempFiles(lTmpFiles);
            lTmpFiles.clear();
        }
        else if(aDataType == dbgexp::CONST_DATA_TYPE_CORES)
        {
            if(base::SvcConfigParams::getInstance()->getIsSimulated() || proc::Svc::isPlatformIfc())
            {
                removeTempFiles(lTmpFiles);
                lTmpFiles.clear();
            }
            else    
            {  
                // Execute this only on real switch, for cores
                std::set<base::String>::iterator iter; 
                for(iter=lTmpFiles.begin(); iter != lTmpFiles.end(); iter++)
                {  
                    LOG_STR(ifc_dbgr, none, LOG_DEBUG4) << "Removing core file=" << (*iter).getBuffer();   
#ifdef DME_NXOS 
                    sysmgr_clear_core_package((*iter).getBuffer());
#endif  
                }  
            }  
        }
    } 


    bool ExportToIFC::
    doExport(base::Uint32 aInVrfId, base::Ip aInDestIp, 
            const base::String& aInSrcFile, const base::String& aInDestFile,
            base::String& aInOutUri)
    {
        LOG_STR(dataexport, none, LOG_DEBUG4) << "In params for export:" << 
                "vrf=" << aInVrfId << ";ip=" << aInDestIp << 
                ";export src=" << aInSrcFile << ";export dest=" << aInDestFile;
        // rsync -8 -avzk -e "ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no" 
        //  file.tgz 10.0.0.1:/data/techsupport/rsyncfile.tgz

        std::ostringstream command;
        base::String lProtocol = PROTOCOL_RSYNC_STR;

        if(!proc::Svc::isPlatformIfc())
        {
            command <<  "LD_PRELOAD=/isan/lib/libsocket.so DCOS_CONTEXT=" << aInVrfId << " ";
        }
        command << lProtocol.getBuffer() << " " <<
                "-8 -avzKL -e \"ssh " <<
                "-o " << SSH_KNOWN_HOSTS_OPT << " " <<
                "-o " << SSH_HOSTKEY_CHECK_OPT << " " <<
                " -i /securedata/ssh/ifc/id_dsa -p 1022 " << 
                " \" " << 
                aInSrcFile.getBuffer() << " " <<
                aInDestIp << ":/" << 
                aInDestFile.getBuffer();

        // CSCur95697: This usage of system is for command formatted completely by the system. 
        // It has no user input, hence is not a security concern. It is a little convulated 
        // to get this working using os::Command due to environment options (LD_PRELOAD) needed 
        // on switch. Please do not reuse this code.
        LOG_STR(dataexport, none, LOG_INFO) << "Executing remote URL " << command.str();
        int lRetval = system(command.str().c_str());
        if(lRetval != 0)
        {
            char errBuf[ERROR_BUFFER_LEN] = {0};
            LOG_STR(dataexport, none, LOG_MAJOR) << "Failed to execute: " <<
                command.str() << ";error=" << strerror_r(errno, errBuf, ERROR_BUFFER_LEN) <<
                "; return value=" << lRetval;
            aInOutUri.clear();
            std::string errCmd = command.str();
            std::replace( errCmd.begin(), errCmd.end(), '"', '\'');
            aStatusStr.append(base::String("Failed to execute "));
            aStatusStr.append(errCmd.c_str());
            aStatusStr.append(base::String(" error "));
            aStatusStr.append(base::String(errBuf));
            return false;
        }
        else
        {
            aStatusStr.append(base::String("Task completed"));
            return true;
        }
        return false;
    }


    int ExportToIFC::
    compressAndTransfer(const base::String& aInCompressionSrcFile, 
            const base::String& aInCompressedFile,
            const base::String& aInRemoteDestFile, 
            const base::String& aInTmpDir, 
            base::Uint32 aInVrfId, base::Ip aInDestIp,
            TechsupFilters aInFilters, 
            base::String& aInOutUri, base::String& aInAppId, bool aInTrimFile)
    {
        int rc = DbgrExportUtils::compressFile(aInCompressionSrcFile, aInCompressedFile, aInTmpDir, aInAppId);
        if(rc == DbgrExportUtils::OPERATION_FAILURE) {
            aStatusStr.append("Failed to compress files.");
            return rc;
        }

        // Change permissions of the compressed file
        if(!DbgrExportUtils::updatePerms(aInCompressedFile)) {
            LOG_STR(dataexport, none, LOG_WARN) << "Failed to set permissions for export file"; 
        }

        // Now find size of compressed file
        LOG_STR(dataexport, none, LOG_DEBUG2) << "Export file name=" << aInCompressedFile;
        struct stat cfile_info;
        if(stat(aInCompressedFile.getBuffer(), &cfile_info))
        {
            char errBuf[ERROR_BUFFER_LEN] = {0};
            LOG_STR(dataexport, none, LOG_MAJOR) << "Failed to open " <<
                    aInCompressedFile << ";error=" << strerror_r(errno, errBuf, ERROR_BUFFER_LEN);
            aStatusStr.append("Failed to compress files.");
            addToCleanup(aInCompressedFile);
            return DbgrExportUtils::OPERATION_FAILURE;
        }

        if(aInTrimFile) {
            // Trim techsupport per filters specified by user
            dbgexp::DbgrExportUtils::trimCompressedFile(aInCompressedFile, 
                        aInFilters.categories, aInFilters.startTime, aInFilters.endTime);
        }

        // Transfer data on IFC
        if(proc::Svc::isPlatformIfc()) {
            if(!doExport(aInVrfId, aInDestIp, aInCompressedFile, aInRemoteDestFile, aInOutUri)) {
                return DbgrExportUtils::OPERATION_FAILURE;
            }
        }
        return rc;
    }


    bool ExportToIFC::
    statInputFile(const base::String& aInFile)
    {
        // stat() did not work well with wildchar, hence using runCommand()
        char *largv[] = {(char*)"ls ", (char*)aInFile.getBuffer(), NULL};
        base::String lStatusStr;
        base::String lOutFile = "/tmp/lscmd.out";
        int lrc = dbgexp::ExportUtils::runCommand("ls", largv, NULL, 
                    lOutFile.getBuffer(), lStatusStr);
        if(lrc != 0) {
            if(aDataType == dbgexp::CONST_DATA_TYPE_CORES)
            {
                LOG_STR(dataexport, none, LOG_MAJOR) << "Failed to find core file " << aInFile;
                aStatusStr = "Failed to find core file ";
                aStatusStr.append(aInFile);
            }
            else
            {
                char errBuf[ERROR_BUFFER_LEN] = {0};
                LOG_STR(dataexport, none, LOG_MAJOR) << "Failed to open file=" <<
                    aInFile << ", error=" << strerror_r(errno, errBuf, ERROR_BUFFER_LEN) <<
                    "; return value=" << lrc;
                aStatusStr = "Failed to find open techsupport file ";
                aStatusStr.append(aInFile);
            }
            return false;
        }
        if(remove(lOutFile.getBuffer()) != 0) {
            LOG_STR(dataexport, none, LOG_WARN) << "Failed to remove " << lOutFile;
        }
        return true;
    }


    void ExportToIFC::
    initiateAndTransfer(mo::Dn& aInPolicyDn, mo::ClassId aInClassId,
            ExportInfo aInInfo, uint64_t aInWindowStartMs,
            const pki::WebTokenDataMo* aInWebTokenData,
            TechsupFilters aInFilters, bool aInUpgradeLogs)
    {
        if(aInClassId == dbgexp::CorePMo::ID)
        {
            aDataType = dbgexp::CONST_DATA_TYPE_CORES;
        }
        else if(aInClassId == dbgexp::TechSupPMo::ID || aInClassId == dbgexp::TechSupOnDMo::ID)
        {
            aDataType = dbgexp::CONST_DATA_TYPE_TECH_SUPPORT;
        }

        mon::MaximumRetryCount currRetryCount = 0;
        int rc;
        while(currRetryCount < aInInfo.maxRetryCount)
        {
            rc = exportData(aInPolicyDn, aInClassId, aInInfo.compression, aInInfo, 
                    aInWindowStartMs, aInInfo.vrfId, aInInfo.srcIp, aInWebTokenData, aInFilters, 
                    aInUpgradeLogs);
            if(rc != DbgrExportUtils::OPERATION_FAILURE)
            {
                if(!proc::Svc::isPlatformIfc()) {
                    if(aDataType == dbgexp::CONST_DATA_TYPE_TECH_SUPPORT) { 
                        addToCleanup(aInInfo.logSrcFile);
                        addToCleanup(DbgrExportUtils::getNxosTechsupPath());
                    }
                }
                else {
                    addToCleanup(aInInfo.logSrcFile);
                }
                addToCleanup(aInInfo.cliSrcFile);
                addToCleanup(aInInfo.tmpDir);
                addToCleanup(aInInfo.cliOutDir);
                if(proc::Svc::isPlatformIfc()) {
                    aStatus = dbgexp::CONST_EXPORT_STATUS_SUCCESS;
                }
                else {
                    aStatus = dbgexp::CONST_EXPORT_STATUS_PENDING;
                }
                if(rc == DbgrExportUtils::OPERATION_PARTIAL_SUCCESS) {
                    aStatusStr.append("; Partial techsupport collected.");
                }
                break;
            }
            else
            {
                LOG_STR(dataexport, none, LOG_MINOR) << "Export task attempt failed. Will retry.";
                aStatusStr.append("Export task attempt failed, retrying attempt #");
                aStatusStr.append(currRetryCount+1);
                DbgrExportUtils::updateSuccessTs(aInPolicyDn, aInWindowStartMs,
                        aStatusUri, aStatusDbUri, aStatusLogsUri, 
                        aConfigSize, aDbSize, aLogsSize, 
                        aStatus, aStatusStr, aDataType, dbgexp::CONST_OPER_STATE_IN_PROGRESS);
                DEBUG4(dataexport) << "Thread entering sleep: sleep(" << RETRY_TIMEOUT_SEC << ")";
                sleep(RETRY_TIMEOUT_SEC);

                currRetryCount++;
                if(currRetryCount >= aInInfo.maxRetryCount)
                {
                    LOG_STR(dataexport, none, LOG_MINOR)
                       << "Number of retries elapsed. Export task failed.";
                    if(aDataType == dbgexp::CONST_DATA_TYPE_TECH_SUPPORT)
                    {
                        addToCleanup(aInInfo.logSrcFile);
                        addToCleanup(aInInfo.cliSrcFile);
                        addToCleanup(aInInfo.tmpDir);
                        addToCleanup(aInInfo.cliOutDir);
                        addToCleanup(DbgrExportUtils::getNxosTechsupPath());
                    }
                    aStatus = dbgexp::CONST_EXPORT_STATUS_FAILED;
                    break;
                }
            }
            cleanup();
        }

        if(aDataType == dbgexp::CONST_DATA_TYPE_CORES && 
                !proc::Svc::isPlatformIfc() &&
                aStatus == dbgexp::CONST_EXPORT_STATUS_FAILED) {
            //XXX: should I write a .FAIL file instead
            corefile::CoreUtils::updateCoreLocation(aInInfo.logSrcFile, 
                    aInWindowStartMs, aInInfo.coreDn, aStatus);
        }

        cleanup();
        LOG_STR(dataexport, none, LOG_DEBUG4) << "Updating status and timestamps";
        DbgrExportUtils::updateSuccessTs(aInPolicyDn, aInWindowStartMs,
                aStatusUri, aStatusDbUri, aStatusLogsUri, 
                aConfigSize, aDbSize, aLogsSize, 
                aStatus, aStatusStr, aDataType, dbgexp::CONST_OPER_STATE_COMPLETED);
    }


    int ExportToIFC::
    exportData(mo::Dn& aInPolicyDn, mo::ClassId aInClassId,
            mon::Compression aInCompression,
            ExportInfo aInInfo, uint64_t aInWindowStartMs,
            base::Uint32 aInVrfId, address::IPv4 aInSrcIp,
            const pki::WebTokenDataMo* aInWebTokenData,
            TechsupFilters aInFilters, bool aInUpgradeLogs)
    {
        int operationStatus = DbgrExportUtils::OPERATION_FAILURE;
        LOG_STR(dataexport, none, LOG_DEBUG4) << "export data thread id=" << boost::this_thread::get_id();

        base::String lCompressionSrcFile = aInInfo.logSrcFile;
        ///base::String lCliSrcFile = aInInfo.cliSrcFile;
        base::String lTmpDir = aInInfo.tmpDir;

        // reset status attributes
        aStatusUri.clear();
        aStatusDbUri.clear();
        aStatusLogsUri.clear();
        aStatus = dbgexp::CONST_EXPORT_STATUS_PENDING;
        aStatusStr = "Triggered export, pending collection";
        base::String lAppId = aInInfo.vendorName;
        lAppId.append("_");
        lAppId.append(aInInfo.appName);

        // stat input file
        if(!statInputFile(lCompressionSrcFile)) {
            return operationStatus;
        }

        // get destination IFC IP and ID
        base::Ip lDestIp;
        frmwrk_addrss::Appliance::Id lApplId;
        getDestIFC(lApplId, lDestIp);


        dbgexp::ExportMeta meta;
        meta.appId = lApplId;
        meta.policyDn = aInPolicyDn.toString().getBuffer();
        meta.collectionTimeMs = aInWindowStartMs;

        if(aDataType == dbgexp::CONST_DATA_TYPE_TECH_SUPPORT) {

            meta.dataType = "techsupport";

            /*
             * CSCuu44695: Write a manifest file 
             */
            base::String lManifestDir, lManifestPath;
            DbgrExportUtils::getManifestPath(aInWindowStartMs, lManifestDir, lManifestPath);
            if(mkdir(lManifestDir.getBuffer(), S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH) == 0) {
                DbgrExportUtils::populateManifest(lManifestPath, aInWindowStartMs, 
                            aInFilters.startTime, aInFilters.endTime);
            }
            else {
                LOG_STR(dataexport, none, LOG_ERROR) << "Failed to create manifest dir " << lManifestDir;
            }

            /*
             * Config:
             *  Add manifest to config file
             *  construct local and remote file names
             *  update status
             *  execute commands to get data
             *  compress and transfer data
             */
            base::String lCompressedFileNameOnly; 
            base::String lCompressedFile; 
            base::String lRemoteDestFile; 
            base::String lSuffix="1of3";
            if (aInInfo.appName.getSize())
                lSuffix="";
            constructFilenames(aInPolicyDn, aInWindowStartMs, lApplId, lSuffix, 
                    lCompressionSrcFile, lCompressedFileNameOnly, lCompressedFile, 
                    lRemoteDestFile, aStatusUri);
            LOG_STR(dataexport, none, LOG_DEBUG4) << "compressed file=" << lCompressedFile
                    << "; uri=" << aStatusUri;

            // Update meta information
            meta.exportSrcFile = lCompressedFile.getBuffer();
            meta.exportSrcFileNameOnly = lCompressedFileNameOnly.getBuffer(); 

            aStatusStr = "Running bash commands";
            DbgrExportUtils::updateSuccessTs(aInPolicyDn, aInWindowStartMs,
                    aStatus, aStatusStr, aDataType, dbgexp::CONST_OPER_STATE_IN_PROGRESS);
 
            aStatusStr.clear();
            bool retryCount = 0, rc = false;
            int retval = DbgrExportUtils::OPERATION_FAILURE;
            base::String lCliResult = ExportUtils::CLI_OUTPUT_FILE;
            while(retryCount < MAX_RETRY_COUNT && rc == false) {
                rc = ExportUtils::executeCLI(aInWebTokenData, aInInfo.cliSrcFile, 
                        lCliResult, aInInfo.cliOutDir, aStatusStr);
                retryCount++;
            }
            if(rc == false) {
                aStatusStr.append(";Skipping failed system config collection.");
                aStatusUri = "Config collection failed";
                aConfigSize = 0;
            }
            else {
                aStatusStr.append("Compressing system config before transfer");
                DbgrExportUtils::updateSuccessTs(aInPolicyDn, aInWindowStartMs,
                        aStatus, aStatusStr, aDataType, dbgexp::CONST_OPER_STATE_IN_PROGRESS);

                aStatusStr.clear();

                retval = compressAndTransfer(lCompressionSrcFile, lCompressedFile, 
                        lRemoteDestFile, lTmpDir, aInVrfId, lDestIp, aInFilters, aStatusUri, lAppId);
                if(retval == DbgrExportUtils::OPERATION_FAILURE) {
                    aStatusUri = "Compress or transfer system config failed";
                    aConfigSize = 0;
                } else {
                    aStatusStr = "Transferred system config.";
                    meta.configUri = aStatusUri.getBuffer();
                    aConfigSize = ExportUtils::getFileSize(lCompressedFile);
                    meta.configSize = aConfigSize;
                }
                operationStatus = retval;
            }

            if(proc::Svc::isPlatformIfc()) {
                interimCleanup(lCompressedFile.getBuffer());
            }
            interimCleanup(lCliResult.getBuffer());
            interimCleanup(aInInfo.cliOutDir, false);
            LOG_STR(dataexport, none, LOG_DEBUG4) << "appName =" << aInInfo.appName ;
            if (aInInfo.appName.getSize())
                return operationStatus;

            /*
             * Database:
             *  construct local and remote file names
             *  update status
             *  execute commands to snapshot DB
             *  compress and transfer DBs
             */
            lCompressedFile.clear();
            lRemoteDestFile.clear();
             
            std::ofstream file;
            file.open(lCompressionSrcFile.getBuffer(), std::ofstream::out | std::ofstream::trunc);
            file << lManifestPath << std::endl; 
            file << base::SvcConfigParams::getInstance()->getDebugMitDbPath() << std::endl;
            file.close();

            lSuffix = "db_2of3";
            base::String lUri;
            constructFilenames(aInPolicyDn, aInWindowStartMs, lApplId, lSuffix, 
                    lCompressionSrcFile, lCompressedFileNameOnly, lCompressedFile, 
                    lRemoteDestFile, aStatusDbUri);
            LOG_STR(dataexport, none, LOG_DEBUG4) << "db compressed file=" << lCompressedFile
                    << "; uri=" << aStatusDbUri;

            aStatusStr.append("Snapshotting database");
            DbgrExportUtils::updateSuccessTs(aInPolicyDn, aInWindowStartMs,
                    aStatusUri, lUri, lUri, 
                    aConfigSize, aDbSize, aLogsSize, 
                    aStatus, aStatusStr, aDataType, dbgexp::CONST_OPER_STATE_IN_PROGRESS);

            aStatusStr.clear();
            rc = ExportUtils::snapshotLocalDbs(aInWebTokenData, aStatusStr);
            if(rc == false) {
                aStatusStr.append("; Failed to snapshot databases");
                aStatusDbUri = "Database snapshot failed";
                aDbSize = 0;
            } else {
                aStatusStr.append("Compressing db snapshot before transfer");
                DbgrExportUtils::updateSuccessTs(aInPolicyDn, aInWindowStartMs,
                        aStatusUri, lUri, lUri, 
                        aStatus, aStatusStr, aDataType, dbgexp::CONST_OPER_STATE_IN_PROGRESS);

                aStatusStr.clear();
                retval = compressAndTransfer(lCompressionSrcFile, lCompressedFile, 
                        lRemoteDestFile, lTmpDir, aInVrfId, lDestIp, aInFilters, aStatusDbUri, lAppId);
                if(retval == DbgrExportUtils::OPERATION_FAILURE) {
                    aStatusDbUri = "Compress or transfer database snapshot failed";
                    aDbSize = 0;
                    operationStatus = retval;
                } else if (retval == DbgrExportUtils::OPERATION_PARTIAL_SUCCESS) {
                    operationStatus = DbgrExportUtils::OPERATION_PARTIAL_SUCCESS;
                } else {
                    aStatusStr = "Transferred database snapshot.";
                    meta.dbUri = aStatusDbUri.getBuffer();
                    aDbSize = ExportUtils::getFileSize(lCompressedFile);
                    meta.dbSize = aDbSize; 
                }
            }
            if(proc::Svc::isPlatformIfc()) {
                interimCleanup(lCompressedFile.getBuffer());
            }
            interimCleanup(base::SvcConfigParams::getInstance()->getDebugMitDbPath());
 

            /*
             * Logs:
             *  construct local and remote file names
             *  update status
             *  compress and transfer DBs
             */
            lCompressedFile.clear();
            lRemoteDestFile.clear();

            DbgrExportUtils::populateLogPaths(lCompressionSrcFile, aInUpgradeLogs, lManifestPath);

            lSuffix = "logs_3of3";
            constructFilenames(aInPolicyDn, aInWindowStartMs, lApplId, lSuffix, 
                    lCompressionSrcFile, lCompressedFileNameOnly, lCompressedFile, 
                    lRemoteDestFile, aStatusLogsUri);
            LOG_STR(dataexport, none, LOG_DEBUG4) << "log compressed file=" << lCompressedFile
                    << "; uri=" << aStatusLogsUri;

            aStatusStr.append("Compressing logs before transfer.");
            DbgrExportUtils::updateSuccessTs(aInPolicyDn, aInWindowStartMs,
                    aStatusUri, aStatusDbUri, lUri, 
                    aConfigSize, aDbSize, aLogsSize, 
                    aStatus, aStatusStr, aDataType, dbgexp::CONST_OPER_STATE_IN_PROGRESS);

            aStatusStr.clear();
            retval = compressAndTransfer(lCompressionSrcFile, lCompressedFile, 
                    lRemoteDestFile, lTmpDir, aInVrfId, lDestIp, aInFilters, aStatusLogsUri, lAppId, true);
            if(retval == DbgrExportUtils::OPERATION_FAILURE) {
                aStatusLogsUri = "Compress or transfer of logs failed";
                aLogsSize = 0;
                operationStatus = retval;
            } else if (retval == DbgrExportUtils::OPERATION_PARTIAL_SUCCESS) {
                operationStatus = DbgrExportUtils::OPERATION_PARTIAL_SUCCESS;
            }
            meta.logsUri = aStatusLogsUri.getBuffer();
            aLogsSize = ExportUtils::getFileSize(lCompressedFile);
            meta.logsSize = aLogsSize;
            if(proc::Svc::isPlatformIfc()) {
                addToCleanup(lCompressedFile); 
            }
            addToCleanup(lManifestDir);

            // Write metadata file on leaf
            if(!proc::Svc::isPlatformIfc() && 
                    operationStatus != DbgrExportUtils::OPERATION_FAILURE) {
               bool rv = DbgrExportUtils::writeMetadata(meta);
                if(rv) {
                   aStatusStr.append("Waiting for APIC to pull file."); 
                } else {
                    aStatusLogsUri.clear();
                    aStatusStr.append(base::String("Failed to write metadata file"));
                    operationStatus = DbgrExportUtils::OPERATION_FAILURE;
                    addToCleanup(lCompressedFile); 
                }
            }
            
            return operationStatus;

        } 

        else if(aDataType == dbgexp::CONST_DATA_TYPE_CORES) {

            // construct remote file name
            base::String lCompressedFileNameOnly; 
            base::String lCompressedFile; 
            base::String lRemoteDestFile; 
            base::String lSuffix="";
            constructFilenames(aInPolicyDn, aInWindowStartMs, lApplId, lSuffix, 
                    lCompressionSrcFile, lCompressedFileNameOnly, lCompressedFile, 
                    lRemoteDestFile, aStatusUri);
            LOG_STR(dataexport, none, LOG_DEBUG4) << "compressed core file=" << lCompressedFile
                    << "; uri=" << aStatusUri;

            // update permissions
            if(!DbgrExportUtils::updatePerms(lCompressionSrcFile)) {
                LOG_STR(dataexport, none, LOG_WARN) << "Failed to set permissions for file" << 
                    lCompressionSrcFile; 
            }

            // transfer file
            aStatusStr.clear();
            if(proc::Svc::isPlatformIfc()) {
                if(doExport(aInVrfId, lDestIp, lCompressionSrcFile, lRemoteDestFile, aStatusUri)) {
                    aConfigSize = ExportUtils::getFileSize(lCompressionSrcFile);
                    return DbgrExportUtils::OPERATION_SUCCESS;
                } else {
                    return DbgrExportUtils::OPERATION_FAILURE;
                }
            }
            else {
                aConfigSize = ExportUtils::getFileSize(lCompressionSrcFile);
                // Write metadata file
                meta.dataType = "cores";
                meta.exportSrcFile = lCompressedFile.getBuffer();
                meta.exportSrcFileNameOnly = lCompressedFileNameOnly.getBuffer(); 
                meta.configUri = aStatusUri.getBuffer();
                meta.configSize = aConfigSize; 
                meta.coreDn = aInInfo.coreDn.toString().getBuffer();
                bool rv = DbgrExportUtils::writeMetadata(meta);
                if(!rv) {
                    aStatusUri.clear();
                    aStatusStr.append(base::String("Failed to write metadata file"));
                    return DbgrExportUtils::OPERATION_FAILURE;
                }
                aStatusStr.append("Waiting for APIC to pull file."); 
                return DbgrExportUtils::OPERATION_SUCCESS;
            }
        }
        return DbgrExportUtils::OPERATION_FAILURE;
    }


} /* namespace dbgexp */