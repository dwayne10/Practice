class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return

        # NOTICE that the length of the rows
        # is different for each row - construct dp array carefully
        dp = [[0] * len(row) for row in triangle]

        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][0] = triangle[i][0] + dp[i - 1][0]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + \
                               triangle[i][j]

        return min(dp[len(triangle) - 1])