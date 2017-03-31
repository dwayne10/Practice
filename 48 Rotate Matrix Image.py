class Solution(object):

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        cols = n

        start = 0
        end = n - 1
        while end - start >= 1:
            for offset in range(end - start):
                # top to right
                temp = matrix[start][start + offset]
                matrix[start + offset][end], temp = temp, matrix[start + offset][end]

                # right to bottom
                matrix[end][end - offset], temp = temp, matrix[end][end - offset]

                # bottom to left
                matrix[end - offset][start], temp = temp, matrix[end - offset][start]

                # left to top
                matrix[start][
                    start + offset], temp = temp, matrix[start][start + offset]
                print(matrix)
            start += 1
            end -= 1
        print("done", matrix)


print(Solution().rotate(
    [[5, 2, 1, 4], [3, 10, 7, 22], [12, 6, 3, 5], [8, 10, 2, 9]]))
