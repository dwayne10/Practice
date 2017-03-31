def searchInSorted2DArray(matrix, target):
    rows = len(matrix) - 1
    col = len(matrix[0]) - 1

    r = c = 0 # start from matrix[0][0]
    while r < rows and col >=0:
        if matrix[r][c] == target:
            return True
        if matrix[r][col] < target:
            # max of this row is lesser than the target
            # therefore cannot be in this row
            print("Eliminating row")
            r += 1
        elif matrix[r][col] > target:
            # value in this column is greater than the target
            # therefore cannot be in this column
            col -= 1
        # if it reached here it means we need to investigate this row
        '''

        NO WE DONT everything below this is unnecessary as the col or row is
        already incremented/ decremented
        If a row is 1 5 5 9 21 and target is 7 at each step we remove a col
        and move leftwards. SEE IMPROVED CODE BELOW !!!!!!!!!!!
        '''
        lo_c = 0
        high_c = col
        while lo_c <= high_c:
            mid = lo_c + (high_c - lo_c)//2
            print("r and mid are:", r, "   ", mid)
            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] < target:
                lo_c = mid + 1
            else:
                high_c = mid - 1
                # cannot exist in this column
                col -= 1
        # not found in this row
        # eliminate this row
        r += 1
    return False

def searchInSorted2DArrayImproved(matrix, target):
    rows = len(matrix) - 1
    col = len(matrix[0]) - 1

    r = 0 # start from matrix[0][0]
    while r <= rows and col >=0:
        if matrix[r][col] == target:
            return True
        if matrix[r][col] < target:
            # max of this row is lesser than the target
            # therefore cannot be in this row
            r += 1
        elif matrix[r][col] > target:
            # value in this column is greater than the target
            # therefore cannot be in this column
            col -= 1
    return False



print(searchInSorted2DArrayImproved([[1,2,3], [4,5,6], [7,8,9]], 1))