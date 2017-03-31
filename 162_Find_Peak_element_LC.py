# /**
#  * https://leetcode.com/problems/find-peak-element/
#  *
#  * O(log n) runtime, O(1) space
#  *
#  * solve this question by using Binary Search
#  * for index left to index right, calculate index mid and then compare nums[mid-1], nums[mid] and nums[mid+1]
#  *   1. if nums[mid-1] < nums[mid] < nums[mid+1], then there is a peak in [mid, right]
#  *   2. if nums[mid-1] < nums[mid] && nums[mid] > nums[mid+1], then nums[mid] is a peak
#  *   3. if nums[mid-1] > nums[mid] && nums[mid] < nums[mid+1], then there is a peak in [mid, right] (or [left, mid])
#  *   4. if nums[mid-1] > nums[mid] > nums[mid+1], then there is a peak in [left, mid]
#  *



class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return nums
        if len(nums) == 1:
            return 0
        # prev = nums[0]
        # if nums[0] > nums[1]: # index 0 element could be peak
        #     return 0
        # return binaryHelper(0, len(nums)-1, nums)



        start = 0
        end = len(nums) - 1

        while start + 1 < end:  # atleast 3 items
            mid = start + (end - start) // 2

            if nums[mid] > nums[mid + 1]:
                if nums[mid - 1] < nums[mid]:
                    return mid
                else:
                    end = mid
            else:
                start = mid

        # there might be the case where only 2 elements are left
        # this is either the first element case or last element case
        if nums[start] > nums[end]:
            return start # index 0
        else:
            return end # last index


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return nums
        if len(nums) == 1:
            return 0

        start = 0
        end = len(nums) - 1

        while start < end:  # atleast 3 items
            mid = start + (end - start) // 2

            if nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid

        return start