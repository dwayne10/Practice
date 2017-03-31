def searchForEqualIndex(nums):
    if not nums:
        return
    left, right = 0, len(nums) - 1
    ret = -1
    while left <= right:
        mid = left + (right - left)//2
        if nums[mid] == mid:
            return mid
        elif nums[mid] < mid:
            # search right side to see if greater index exists
            # ret = mid
            left = mid + 1
        elif nums[mid] > mid:
            right = mid - 1
    return -1

print(searchForEqualIndex([0,1,2,3]))