class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        i = 0
        j = len(matrix[0]) - 1 # last element of a row
        if j < 0:
            return False
        while i < len(matrix):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                # move row forward
                i += 1
            else:
                if matrix[i][0] > target:
                    # no point checking
                    return False
                # do binary search on this row
                l = 0
                h = j
                while l <= h:
                    mid = l + (h - l)//2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        h = mid - 1
                    else:
                        l = mid + 1
                return False
        return False


    