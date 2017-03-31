class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        cols = len(grid[0])
        dp = [0 for _ in range(cols)]
        dp[0] = 1
        for row in grid:
            for j in range(cols):
                if row[j] == 1:
                    # obstacle
                    dp[j] = 0
                elif j > 0:
                    """
                    dp[j] = dp[j] + dp[j - 1];
                    which is new dp[j] = old dp[j] + dp[j-1]
                    which is current cell = top cell + left cell
                    """
                    dp[j] = dp[j] + dp[j - 1]
        return dp[cols - 1]



grid = [
  [0,0,0,0],
  [0,0,1,0],
  [0,0,0,0]
]
print(Solution().uniquePathsWithObstacles(grid))