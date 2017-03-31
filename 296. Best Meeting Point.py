class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        houses = []
        x = []
        y = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x.append(i)
                    y.append(j)
                    houses.append([i, j])

        # x.sort() technically this isnt needed for rows as its already being
        # added in the sorted order due to the two loops
        y.sort()

        x1 = 0.0
        y1 = 0.0
        if len(x) % 2 == 0:
            x1 = (x[len(x) // 2] + x[len(x) // 2 - 1]) * 0.5
            y1 = (y[len(y) // 2] + y[len(y) // 2 - 1]) * 0.5
        else:
            x1 = x[len(x) // 2]
            y1 = y[len(y) // 2]

        res = 0
        for house in houses:
            res += abs(house[0] - x1) + abs(house[1] - y1)
        return int(res)
