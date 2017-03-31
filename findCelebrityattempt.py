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
        row = 0
        col = 1
        # row and column cannot be same as that would be knows(a,a) which does not make sense
        while col < n:
            if knows(row,col):
                # this means row knows col therefore row cannot be celeb
                row = col 
                col += 1 
            else:
                # col cannot be celeb, row can still be the celeb
                col += 1
        return row 
        