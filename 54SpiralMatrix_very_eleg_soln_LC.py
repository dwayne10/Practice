class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        rows = len(matrix)
        cols = len(matrix[0])
        res = matrix[0]
        total = (rows - 1) * cols # rows - 1 because we are directly appending first row to the res
         # no need to traverse the first row of the matrix
        x_y = [0, cols - 1] # x and y - we are starting at top right index
        offsets =[[1,0], [0,-1] , [-1,0], [0,1] ]
        
        d = 0 # d keeps track of position in offsets. we keep switching between horizontal iteration and vertical iteration

        while total > 0:
            for j in range(1,rows):
                total -= 1 
                x_y[0] = x_y[0] + offsets[d][0] 
                x_y[1] = x_y[1] + offsets[d][1]
                res.append(matrix[x_y[0]][x_y[1]])
            
            rows -= 1
            # switch directions
            rows, cols = cols, rows # swap val of rows and cols 
            d += 1
            d = d % 4
        return res
            
            