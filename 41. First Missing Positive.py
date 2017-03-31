class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] < len(nums) and nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

        j = 0
        while j < len(nums):
            if nums[j] != j + 1:
                return j + 1
            j += 1

        return len(nums) + 1

