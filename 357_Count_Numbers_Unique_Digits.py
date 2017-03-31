class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n or n == 0:
            return 1

        if n == 1:
            return 10

        '''
        # My solution here - not very elegant and O(n) space
        res = [None]*(n+1)
        res[0] = 0
        res[1] = 10 # 10 choices for n = 1
        res[2] = 81 # 9 * 9 for n == 2
        seed = 8

        for length in range(3,n+1):

            res[length] = res[length-1]*seed
            seed -= 1

        return sum(res)
        '''
        res = 10
        unique = 9
        available = 9
        for length in range(2, n + 1):
            unique = unique * available
            res = res + unique
            available -= 1

        return res
