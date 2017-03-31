def firstOccurance(nums, target):
    if not nums:
        return None
    low, high = 0, len(nums) - 1
    ret = -1
    while low <= high:
        mid = low + (high - low)//2
        if nums[mid] == target:
            # search left side to see if lesser index
            ret = mid
            high = mid - 1
        elif nums[mid] < target:
            # search RHS
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
    return ret

print(firstOccurance([2,3,6,6,7], 6))
