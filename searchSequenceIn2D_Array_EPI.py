def isPattenInGrid(g, p):
    def checkPatternAtXY(grid, x, y, pattern, suffix_index, prev_attempts):
        if len(pattern) == suffix_index:
            # nothing left to check
            return True

        # Check if x and y are valid and if this attempt has already been made
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or (x,y, suffix_index) in prev_attempts:
            return False

        if grid[x][y] == pattern[suffix_index] and (checkPatternAtXY(grid,
                                                                     x+1, y, pattern, suffix_index+1, prev_attempts) or checkPatternAtXY(grid, x,
                                                                                                            y+1,
                                                                                                            pattern,
                                                                                                            suffix_index+1, prev_attempts) or checkPatternAtXY(grid, x-1, y, pattern, suffix_index+1, prev_attempts) or checkPatternAtXY(grid, x, y-1, pattern, suffix_index+1, prev_attempts)):
            return True

            # there is match
            # now check if any of the neighbors has the next suffix index value
        if (x,y, suffix_index) not in prev_attempts:
            prev_attempts.append((x,y,suffix_index))
        #this was a failed attempt so return False
        return False


    prev_attempts = [(None,None,None)]
    for r in range(len(g)):
        for c in range(len(g[0])):
            if checkPatternAtXY(g, r, c, p, 0, prev_attempts) :
                return True
    return False

matrix = [[1,2,3], [3,4,5], [5,6,7]]
find = [1,2,3,4]
print(isPattenInGrid(matrix, find))