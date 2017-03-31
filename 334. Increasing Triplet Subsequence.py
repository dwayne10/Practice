class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 3:
            return False

        # dp = [1] * len(nums)

        # This is using the idea of Longest Increasing Seq
        # but this is O(n2) in the worst case : i.e its a constantly decreasing array
        # This causes Time Limit Exceeded
        # for i in range(1,len(nums)):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], 1 + dp[j])
        #             if dp[i] == 3:
        #                 return True
        # return False

        # Instead we can do this in one pass i.e O(n)

        level1 = level2 = float('inf')

        for num in nums:
            if num <= level1:
                level1 = num
            elif num <= level2:
                level2 = num
            else:
                # this num is greater than two numbers
                # automatically meaning there are there is a triplet
                return True

        return False
