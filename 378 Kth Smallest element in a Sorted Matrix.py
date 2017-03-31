from heapq import *

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return


        minheap = []
        '''
            Naive way:
            Push all elements onto a minheap
            Pop each element and decrement k each time

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heappush(minheap, matrix[i][j])

        while k != 0 and len(minheap) > 0:
            num = heappop(minheap)
            k -= 1
        return num
        '''

        '''
            Better way push either just the first row or first column onto the minheap
            Then for k - 1 times pop an item and add the next item from its column
            At any point of time there will be a maximum of n items on the heap
            where n is the number of cols/number of rows
        '''
        # push elements of first row onto heap
        for c in range(len(matrix[0])):
            heappush(minheap, (matrix[0][c], 0, c))

        '''
            for i from 0 to k - 1 pop items from heap.
            replace with next element in that element's col
        '''

        for _ in range(1, k):  # i.e do it k - 1 times
            val, i, j = heappop(minheap)
            if i == len(matrix) - 1:
                # i.e on the last row so cannot do heappush of next row
                continue

            # add item from last popped item's next row, same column
            heappush(minheap, (matrix[i + 1][j], i + 1, j))

        # now the kth smallest one is at the top of the heap
        # pop it and return

        res, i, j = heappop(minheap)

        return res