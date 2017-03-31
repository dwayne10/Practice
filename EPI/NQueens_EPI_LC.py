class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def helper(n, current_row):
            if current_row == n:
                print("perm is: ", perm)
                res.append(perm[:])
                print(res)
                # return None
            else:
                for c in range(n):
                    perm.append(c)
                    if isValid(perm):
                        helper(n, current_row + 1)
                    perm.pop()

        def isValid(attempt):
            c_row = len(attempt) - 1
            for i in range(c_row):
                diff = abs(perm[c_row] - perm[i])
                if diff == 0 or diff == c_row - i:
                    return False
            return True

        res = []
        perm = []
        helper(n, 0)
        print(res)


Solution().solveNQueens(4)