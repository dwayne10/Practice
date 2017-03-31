def firstOccuranceGreaterThanK(nums, target):
    '''
    Find the last occurance of target and add 1 to the res to get index of
    the element greater than target

    :param nums:
    :param target:
    :return:
    '''
    if not nums:
        return None
    left, right = 0, len(nums) - 1
    ret = -1
    while left <= right:
        mid = left + (right - left)//2
        if nums[mid] <= target:
            # search right side to see if greater index exists
            ret = mid
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return ret + 1 if ret + 1 < len(nums) else -1

print(firstOccuranceGreaterThanK([-14,-10,2,108,108,243,285,285,285,401], 401))