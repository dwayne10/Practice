class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        graph = Graph(grid)
        return self.countHelper(graph)

    def isValid(self, x, y, graph):
        return (x >= 0 and y >= 0 and x < graph.rows and y < graph.cols and
                graph.visited[x][y] == False and graph.g[x][y] == "1")

    def DFS(self, i, j, graph):
        graph.visited[i][j] = True

        # N, E, S, W directions order
        directions_x = [-1, 0, 1, 0]
        directions_y = [0, 1, 0, -1]

        for k in range(4):
            if self.isValid(i + directions_x[k], j + directions_y[k], graph):
                self.DFS(i + directions_x[k], j + directions_y[k], graph)

    def countHelper(self, graph):

        count = 0
        for i in range(graph.rows):
            for j in range(graph.cols):

                if graph.visited[i][j] == False and graph.g[i][j] == "1":
                    self.DFS(i, j, graph)
                    count += 1
        return count


class Graph:
    def __init__(self, grid):
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.g = grid
        self.visited = [[False] * self.cols for _ in range(self.rows)]