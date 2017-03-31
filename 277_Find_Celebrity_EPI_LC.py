# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """

        '''
        Take advantage of the knows matrix and move through that
        Think of it as searching through the knows matrix
        '''
        # row = 0
        # col = 1
        # row and column cannot be same as that would be knows(a,a) which does not make sense

        i = 0  # i starts as the first row
        j = 1  # j starts as the second col, since cannot be same as j
        for j in range(1, n):
            if knows(i,j):
                # if i knows someone , i cannot be in the celebrity. need to change i
                # on the other hand, since i does not know j, j could be the celebrity
                i = j

        # i is now the potential celeb candidate
        # it is either him or -1

        # now have to see if there is i knows anyone
        # if he does he is not a celebrity so return -1

        for col in range(i):
            if knows(i, col):
                return -1

        # now have to check if anyone DOES NOT know i
        # if someone does not know i he is immediately not the celeb

        for row in range(
                n):  # important that here it is n as range. we need to check every row againt i
            if not knows(row, i):
                return -1
        return i