class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        # NOTE: input is a list of strings
        # dp[0] = [int(x) for x in matrix[0]]

        maxi = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i == 0 or j == 0) and matrix[i][j] == "1":
                    dp[i][j] = 1
                elif matrix[i][j] == "1":
                    dp[i][j] = min(min(dp[i - 1][j], dp[i - 1][j - 1]),
                                   dp[i][j - 1]) + 1
                maxi = max(maxi, dp[i][j])

        return maxi * maxi
