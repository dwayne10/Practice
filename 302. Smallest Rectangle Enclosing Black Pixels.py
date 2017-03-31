class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """

        def isValid(i, j):
            return i >= 0 and i < len(image) and j >= 0 and j < len(
                image[0]) and visited[i][j] == False and image[i][j] == "1"

        def dfs(i, j):

            visited[i][j] = True

            # N, S, E, W
            offsets_x = [-1, 1, 0, 0]
            offsets_y = [0, 0, 1, -1]
            for k in range(4):  # offsets
                if isValid(i + offsets_x[k], j + offsets_y[k]):
                    all_x.append(i + offsets_x[k])
                    all_y.append(j + offsets_y[k])
                    dfs(i + offsets_x[k], j + offsets_y[k])

        if not image:
            return 0

        all_x = [x]
        all_y = [y]
        visited = [[False] * len(image[0]) for _ in range(len(image))]
        dfs(x, y)

        breadth = max(all_x) - min(all_x) + 1
        length = max(all_y) - min(all_y) + 1

        return length * breadth
