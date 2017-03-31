class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        row = 0
        col = len(matrix[0]) - 1

        '''
        Logic : Only need to compare with last element in the row
        If target larger than last element in the row then the whole row wont have it
        If target is lesser than last element in the row , then the col containing the last element
        cannot have this target as all the elements below it are larger

        So at each iteration either one row or one column is discarded
        '''
        while row < len(matrix) and col >= 0:
            if target > matrix[row][col]:
                # cannot be in this row
                # as rightmost is the largest item
                # and the target is larger than that 
                
                row += 1
            elif target < matrix[row][col]:
                # cannot be in this column anymore
                # as every item below this is larger
                
                col -= 1
            else:
                return True
        return False

