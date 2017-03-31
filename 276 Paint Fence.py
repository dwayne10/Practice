class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        if n == 0:
            return 0

        if n == 1:
            return k

            # n = 2 case
        same = k  # k for 1st house, 1 choice for 2nd house so k*1
        diff = k * (k - 1)  # k choices for 1st, k - 1 choices for 2nd so k * (k - 1)

        for f in range(3, n + 1):
            prev_same = same
            same = diff
            diff = (prev_same * (k - 1)) + (diff * (k - 1))

        return same + diff