class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        def isValid(x, y, x0, y0):
            return x >= 0 and y >= 0 and x < len(matrix) and y < len(matrix[0]) and matrix[x][y] > matrix[x0][y0]

        def dfs(i, j, path, longest):
            visited[i][j] = True
            # N, S, E, W
            offset_x = [-1, 1, 0, 0]
            offset_y = [0, 0, 1, -1]

            for k in range(4):
                next_x = i + offset_x[k]
                next_y = j + offset_y[k]
                if isValid(next_x, next_y, i, j):
                    if visited[next_x][next_y] == False and dp[next_x][next_y] == 0:
                        # Perform dfs only if the cell is not visited
                        dp[i][j] = max(1 + dfs(next_x, next_y, path, longest), dp[i][j])
                    elif visited[next_x][next_y] == True:
                        # Else just pick the value form the cache
                        dp[i][j] = max(1 + dp[next_x][next_y], dp[i][j])

            dp[i][j] = max(dp[i][j], 1)
            return dp[i][j]

        if not matrix:
            return 0
        path = 1
        res = 1
        visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if visited[row][col] == False:
                    res = max(dfs(row, col, path, 1), res)
        return res