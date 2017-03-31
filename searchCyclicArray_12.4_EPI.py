def searchCyclic(nums):
    if not nums:
        return None
    low, high = 0, len(nums) - 1
    ret = -1
    while low <= high:
        mid = low + (high - low)//2
        if nums[mid] > nums[mid+1]:
            # search left side to see if lesser index
            ret = mid
            high = mid - 1
            print("Rotation point is: ", nums[mid+1])
            return mid + 1

        elif nums[low] <= nums[mid] <= nums[high]:
            # its sorted so go left
            high = mid - 1
        elif nums[low] > nums[high]:
            if nums[low] > nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return -1



def searchCyclicEPIVersion(nums):
    if not nums:
        return None
    low, high = 0, len(nums) - 1
    ret = -1
    while low <= high:
        mid = low + (high - low)//2
        if nums[mid] > nums[mid+1]:
            # search left side to see if lesser index
            ret = mid
            high = mid - 1
            print("Rotation point is: ", nums[mid+1])
            return mid + 1

        elif nums[low] <= nums[mid] <= nums[high]:
            # its sorted so go left
            high = mid - 1
        elif nums[low] > nums[high]:
            if nums[low] > nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return -1
print(searchCyclic([1,0,1,1,1]))