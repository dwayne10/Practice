class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        if 0 not in nums:
            return True

        index = len(nums) - 2  # start at last but one index
        min_req = 1  # min number of jumps required
        while index >= 0:
            if nums[index] < min_req:
                # if current index's max jumps is lesser than the minimum
                # add 1 to min number of jumps required
                if index == 0:
                    return False
                min_req += 1
            else:
                min_req = 1
            index -= 1
        return True 