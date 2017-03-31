class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def dfs(string, open, close):
            if len(string) == n * 2:
                res.append(string)
                return

            if open < n:
                dfs(string + "(", open + 1, close)

            if close < open:
                dfs(string + ")", open, close + 1)

        res = []
        maxi = n * 2
        # start_str = "(" # has to start with open bracket
        open = 0
        close = 0
        dfs("", open, close)

        return res


print(Solution().generateParenthesis(3))


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