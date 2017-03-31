from heapq import *


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """

        self.min_heap = []
        self.max_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # python doesnt have a maxheap so have to negate values
        # it has only min-heaps
        # from heapq import *

        heappush(self.max_heap, -num)

        top = self.max_heap[0]

        heappush(self.min_heap, -top)  # balance max and min
        heappop(self.max_heap)

        if len(self.max_heap) < len(self.min_heap):
            # max should always have 1 element or 0 elements MORE than min
            # this bcoze if n is even they will have same heights
            # However if n is odd the median is the top of the max heap
            min_top = heappop(self.min_heap)
            heappush(self.max_heap, -min_top)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) * 0.5


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(5)
param_2 = obj.findMedian()
