class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def helper(row, start, end):
            res.append(row)
            for i in range(start, end):
                helper(row + [nums[i]], i + 1, end)
            return res

        if not nums:
            return []
        res = []

        helper([], 0, len(nums))
        return res