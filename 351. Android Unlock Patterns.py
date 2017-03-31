class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        def isValid(i, last):
            # last is the previous number added to the pattern
            if used[i]:
                # i is already in the pattern
                return False

            if last == -1:
                # first number in pattern
                return True

            # Knight's move or adjacent cells
            # here the sum of cell positions will be odd
            if (i + last) % 2 == 1:
                return True

            if (i + last) / 2 == 4:
                # diagonals i.e 0 and 8 or 2 and 6
                # True only if 4 is already used
                return True if used[4] else False

            if (i / 3 != last / 3) and (i % 3 != last % 3):
                # above line checks if they are in same row or same column
                # if they are not it means they are diagonally adjacent elements
                return True  # diagonal adjacent elements

            # if it reaches here it means they are two numbers on ends of same row or column
            # Eg: 0 and 6
            # 1 and 7. In these case they are valid only if the middle element between them is
            # already in the pattern or not
            # So for 0 and 6 it would be 3. 1 and 7 it would be 4 and so on.
            return used[(i + last) // 2]

        def dfs(rem_length, last):
            if rem_length == 0:
                return 1

            sum_for_this_length = 0
            for cell in range(0, 9):
                if isValid(cell, last):
                    used[cell] = True
                    sum_for_this_length += dfs(rem_length - 1, cell)
                    used[cell] = False  # reset the used

            return sum_for_this_length

        res = 0  # total number of Patterns
        used = [False] * 9
        for length in range(m, n + 1):
            res += dfs(length, -1)
            used = [False] * 9

        return res