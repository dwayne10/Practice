class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict

        map = defaultdict(int)

        for n in nums:
            map[n] += 1

        buckets = [[]] * (len(nums) + 1)

        for n in map:
            freq = map[n]

            if buckets[freq] == []:
                buckets[freq] = [n]
            else:
                buckets[freq].append(n)

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            if len(res) < k and buckets[i] != []:
                res.extend(buckets[i])

        return res


# Method 2 - Using max-heap
from heapq import *
class Solution2(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict


        map = defaultdict(int)

        for n in nums:
            map[n] += 1

        maxheap = []

        for num in map:
            freq = map[num]
            heappush(maxheap, (-freq, num))

        res = []
        while len(res) < k:
            freq, num = heappop(maxheap)
            res.append(num)
        return res

