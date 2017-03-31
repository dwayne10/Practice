class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        i = 0
        j = 0

        while j < len(nums):
            if nums[j] != 0 and nums[i] != 0:
                i += 1
                j += 1
            elif nums[j] == 0 and nums[i] == 0:
                j += 1  # move only j fwd

            else:
                # j is at a non-zero and i is at a zero
                # swap
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1


