def numberofWays(row, col):
    def helper(r, c, number_of_ways):
        print("r and c are: ", r, " ", c)
        if r == 0 and c == 0:
            # base case
            return 1
        if number_of_ways[r][c] == 0:
            # not yet computed. compute recursively
            from_top = 0 if c == 0 else helper(r, c-1, number_of_ways)
            from_left = 0 if r == 0 else helper(r-1, c, number_of_ways)
            # update the matrix now
            number_of_ways[r][c] = from_left + from_top
        return number_of_ways[r][c]

    number_of_ways = [ [0]*col for _ in range(row)] # 2D matrix for storing the counts
    print(helper(row-1, col-1, number_of_ways))


numberofWays(5,5)