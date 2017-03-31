#!/usr/bin/python

# Example Invocation:
#
#/local/gkalele/mgmt.amazon/common/src/dataexport/leafPullJobDispatcher.py -u root -t /var/run/mgmt/log/ -i /securedata/ssh/root/id_dsa -m /data/techsupport -d /var/log/dme/oldlog/ -a 1  -l 10.0.112.95 -q

# The metadata file must contain the data on the first line, separated by ':' characters as below
# APICID:collectionType:policyD:collectionTime:file-location:md5sum

# echo "1:core:policyD:collectionTime:filepath:md5sum" > apic1.xxxxx.JOB;
# echo "AAAAAAAAAAAAAAA" > /var/log/dme/oldlog/xxxxx

from optparse import OptionParser
import os
import os.path
import re
import sys
import time
import tarfile
import tempfile
import subprocess
import urllib2
import threading
import glob

logfilename = "/data/log/dbgr-leafpull.log"
logfile = open(logfilename, "a+")


def parse_options():
    parser = OptionParser()
    parser.add_option("-a", "--appliance", dest="applianceId",
                      help="Our appliance id")
    parser.add_option("-l", "--leaf", dest="leaf",
                      help="destination leaf that will be scanned")
    parser.add_option("-m", "--metadata", dest="metadata",
                      help="metadata directory on destination leaf")
    parser.add_option("-d", "--data", dest="datadir")
    parser.add_option("-i", "--identityfile", dest="identityfile")
    parser.add_option("-b", "--srcintf", dest="srcintf")
    parser.add_option("-u", "--user", dest="user",
                      default="root",
                      help="username for rsync+ssh to leaf")
    parser.add_option("-t", "--tmpdir", dest="tmpdir",
                      help="base directory to create temporary directories")
    parser.add_option("-L", "--lockfile", dest="lockfile",
                      help="Lock file to prevent overlapping jobs",
                      default="running.lock")
    parser.add_option("-p", "--pid", dest="pid",
                      help="PID of parent to watch for aliveness")
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose", default=True,
                      help="turn off verbose mode")

    (options, args) = parser.parse_args()
    # if not options.src or not options.dst or not options.passphrase:
    #    parser.print_help()
    #    sys.exit(1)

    return (options, args)


def rsyncBaseCommand(options):
    quietFlag = "-q"
    if options.verbose:
        quietFlag = ""
    # Keep the connectTimeout very low, to prevent long hangs.
    baseCommand = """/usr/bin/rsync -8 %s -avzkL -e "ssh -b %s -i %s -o UserKnownHostsFile=/dev/null -o GSSAPIAuthentication=no -o StrictHostKeyChecking=no -o ConnectTimeout=5 -o ServerAliveInterval=5" """ % (
        quietFlag, options.srcintf, options.identityfile)
    return baseCommand


def runCommand(cmd):
    # Run a shell command
    # logfile.write("\n%s: Running command %s" %(time.strftime("%H:%M:%S"),
    # cmd))
    print "Running CMD: %s" % cmd
    process = subprocess.Popen(
        args=cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    output = process.communicate()[0]
    # if len(output) > 0:
    #    logfile.write("\nOutput: %s" % output)
    return process.returncode

# Returns an integer representing the percent usage of the disk volume
# FAILSAFE - if we have any trouble in this routine, we return 0% used


def checkDiskSpace(vol, options):

    # Create a different df output file based on the volume we are checking
    baseName = os.path.basename(vol)
    if not baseName:
        print "Invalid volume"
        return 100

    tmpFile = os.path.join(options.tmpdir, "df_output_%s.txt" % baseName)
    # Cleanup old df output so we don't get confused with previous df state
    if os.path.exists(tmpFile):
        try:
            os.remove(tmpFile)
        except:
            pass
    # Execute df -h and parse the output
    cmd = "df -h %s > %s" % (vol, tmpFile)
    runCommand(cmd)

    if not os.path.exists(tmpFile):
        print "df command failed - returning 0 %"
        logfile.write("\n%s: df command failed for %s" %
                      (time.strftime("%H:%M:%S"), vol))
        return 100

    if os.path.getsize(tmpFile) == 0:
        print "df command returned zero byte size"
        logfile.write("\n%s: df command returned zero byte size for %s" %
                      (time.strftime("%H:%M:%S"), vol))
        return 100

    try:
        fd = open(tmpFile, "rt")
        lines = fd.readlines()
        fd.close()
        if len(lines):
            exp = re.compile("\s+(\d+)%\s+")
            for l in lines:
                m = exp.search(l)
                if m:
                    percent = m.group(1)
                    print "Parsed df output as %s" % percent
                    percent = int(percent)
                    print "Conversion to int successful - %d" % percent
                    return percent
    except Exception, e:
        print "Exception %s trying to read df output"
        logfile.write("\n%s: Failed to read df command output for %s" %
                      (time.strftime("%H:%M:%S"), vol))
    return 100


def pullMetadataFiles(options):
    # Run an rsync job with a include/exclude filter to fetch all apicN.*.JOB
    # files
    baseCommand = rsyncBaseCommand(options)
    baseCommand = baseCommand + " %s@%s:%s/apic%s.*.JOB %s/" % (options.user,
                                                                options.leaf,
                                                                options.metadata,
                                                                options.applianceId,
                                                                options.tmpdir)
    logfile.write("\n%s: Pulling files with command %s\n" %
                  (time.strftime("%H:%M:%S"), baseCommand))
    runCommand(baseCommand)

    # Log name of files that were pulled
    filenames = next(os.walk(options.tmpdir))[2]
    for file in filenames:
        logfile.write("%s;" % file)

    # Wipe out old metadata files older than 60 minutes
    # logfile.write("\nDeleting files older than 600 min")
    cmd = "cd %s; find %s -name '*.JOB' -mmin +600 -delete" % (
        options.tmpdir, options.tmpdir)
    runCommand(cmd)
    cmd = "cd %s; find %s -name '*.DONE' -mmin +600 -delete" % (
        options.tmpdir, options.tmpdir)
    runCommand(cmd)
    cmd = "cd %s; find %s -name '*.FAIL' -mmin +600 -delete" % (
        options.tmpdir, options.tmpdir)
    runCommand(cmd)


def pushMetadataFiles(options):
    logfile.write("\nPushing metadata files")
    localCleanupList = []
    baseCommand = rsyncBaseCommand(options)
    baseCommand = baseCommand + " %s/apic%s.*.DONE %s@%s:%s/" % (options.tmpdir,
                                                                 options.applianceId,
                                                                 options.user,
                                                                 options.leaf,
                                                                 options.metadata)
    rc = runCommand(baseCommand)
    if rc == 0:
        localCleanupList.append("%s/apic%s.*.DONE" %
                                (options.tmpdir, options.applianceId))
    baseCommand = rsyncBaseCommand(options)
    baseCommand = baseCommand + " %s/apic%s.*.JOB %s@%s:%s/" % (options.tmpdir,
                                                                options.applianceId,
                                                                options.user,
                                                                options.leaf,
                                                                options.metadata)
    runCommand(baseCommand)
    baseCommand = rsyncBaseCommand(options)
    baseCommand = baseCommand + " %s/apic%s.*.FAIL %s@%s:%s/" % (options.tmpdir,
               logfile.write(
                    "\nERROR: rsync failed; will retry during next run for file %s" % fname)
                print "ERROR: rsync failed - will retry during next run for file %s" % fname
                continue
        else:
            logfile.write("\nDisk full, do not rsync")
            print "DISK FULL condition - do not rsync"

        # Delete the job file so that the next run doesn't pick it up again
        # UNCOMMENT THIS after testing
        cleanupFilelist.append(os.path.join(
            options.metadata, "apic%s.%s.JOB" % (options.applianceId, fname)))
        # localCleanupList.append(os.path.join(options.tmpdir, "apic%s.%s.JOB"
        # % (options.applianceId, fname)))

        jobFile=os.path.join(options.tmpdir, "apic%s.%s.JOB" %
                               (options.applianceId, fname))
        doneFile=os.path.join(
            options.tmpdir, "apic%s.%s.DONE" % (options.applianceId, fname))
        failFile=os.path.join(
            options.tmpdir, "apic%s.%s.FAIL" % (options.applianceId, fname))
        if diskFull:
            os.rename(jobFile, failFile)
        else:
            os.rename(jobFile, doneFile)

    # Cleanup pulled files on the leaf
    deleteRemoteFiles(cleanupFilelist, options)
    # Push THE .DONE or .FAIL files back to the node
    localCleanupList=pushMetadataFiles(options)
    for f in localCleanupList:
        if('*' in f):
            # Handle wildchar expansion
            for file in glob.glob(f):
                logfile.write("\nRemoving %s" % file)
                os.remove(file)
        else:
            logfile.write("\nRemoving %s" % f)
            os.remove(f)


def rotateLogFile():
    stat=os.stat(logfilename)
    if(stat.st_size > 1000000):
        cmd="/usr/sbin/logrotate --state /tmp/logrotate.status /etc/logrotate.d/leafpull"
        runCommand(cmd)


if __name__ == "__main__":
    (options, args)=parse_options()
    rotateLogFile()
    if not os.path.exists(options.tmpdir):
        os.mkdir(options.tmpdir)
    logfile.write("\n%s: Starting data pull job from node %s as user %s" % (
        time.strftime("%H:%M:%S"), options.leaf, options.user))
    print "Starting Data file pull job from node %s - using username %s" % (options.leaf, options.user)
    percent=checkDiskSpace(options.datadir, options)
    percent1=checkDiskSpace(options.metadata, options)
    diskFull=False
    # If either the /data/techsupport or /var/log/dme/oldlog volumes is more
    # than 95% used, fail the jobs
    logfile.write("\nChecking disk full")
    if (percent > 90) or (percent1 > 90):
        diskFull=True
        logfile.write("\n%s: Disk %s(%s) full, %s(%s) full. Failing jobs" % (
            time.strftime("%H:%M:%S"), options.datadir, percent, options.metadata, percent1))
        print "DISK IS FULL - FAILING ALL JOBS FOUND ON NODE %s" % options.leaf

    pullMetadataFiles(options)
    pullRsyncJobs=processJobFiles(options)
    executeRsyncPulls(pullRsyncJobs, options, diskFull)
    logfile.write("\n\n")
    logfile.close()
