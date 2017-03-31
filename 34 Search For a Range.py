class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def search(left, right, target, range):
            if left > right:
                return -1

            mid = left + (right - left) // 2

            if nums[mid] > target:
                search(left, mid - 1, target, range)
            elif nums[mid] < target:
                search(mid + 1, right, target, range)
            else:
                # equal
                if mid < range[0]:
                    range[0] = mid
                    search(left, mid - 1, target, range)
                if mid > range[1]:
                    range[1] = mid
                    search(mid + 1, right, target, range)

        range = [len(nums), -1]
        search(0, len(nums) - 1, target, range)

        if range[0] == len(nums):
            return [-1, -1]

        return range


