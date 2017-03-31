class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def createPalindromeTable(s):
            if not s:
                return []

            res = []

            dp = [[False] * len(s) for _ in range(len(s))]

            for i in range(len(s)):
                dp[i][i] = True

            for i in range(len(s) - 1):
                if s[i] == s[i + 1]:
                    dp[i][i + 1] = True

            for length in range(3, len(s) + 1):
                for i in range(len(s) - length + 1):
                    j = i + length - 1
                    if s[i] == s[j] and dp[i + 1][j - 1] == True:
                        dp[i][j] = True
            return dp

        def backtrack(input, pt, start, res):

            if len(path) > 0 and start >= len(s):
                row = path[:]
                res = min(res, len(row))
                # print(res)

            for i in range(start, len(input)):
                if pt[start][i] is True:
                    path.append(''.join(input[start:i + 1]))
                    res = backtrack(input, pt, i + 1, res)
                    path.pop()

            return res
        palindromeTable = createPalindromeTable(s)

        # res =
        path = []
        res = backtrack(list(s), palindromeTable, 0, float('inf'))

        return res


print(Solution().partition("xxyyzz"))