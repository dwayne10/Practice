class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dp = [[0] * len(nums) for _ in range(len(nums))]

        for i in range(len(nums)):
            if nums[i] >= s:
                return 1
            dp[i][i] = nums[i]

        for length in range(2, len(nums) + 1):
            for i in range(len(nums) - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i][j - 1] + dp[j][j]
                if dp[i][j] >= s:
                    return length

        return 0
