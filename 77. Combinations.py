class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def dfs(nums, last_num):

            if len(nums) == k:
                res.append(nums)

            for i in range(last_num + 1, n + 1):
                dfs(nums + [i], i)

        if not n or not k:
            return []
        res = []

        for i in range(1, n + 1):
            dfs([i], i)
        return res