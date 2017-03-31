# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from heapq import *
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return []

        heap = []
        for list in lists:
            head = list
            while head is not None:
                heappush(heap, head.val)
                head = head.next

        res = []
        while len(heap) > 0:
            res.append(heappop(heap))

        return res



class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def sortAndMerge(list1, list2):
            # base case
            if not list1:
                return list2

            if not list2:
                return list1


            if list1.val <= list2.val:
                res = ListNode(list1.val)
                res.next = sortAndMerge(list1.next, list2)

            else:
                res = ListNode(list2.val)
                res.next = sortAndMerge(list1, list2.next)

            return res

        def iterateLists(lists, k):
            start = 0
            end = k

            while len(lists) > 1:
                lists[start] = sortAndMerge(lists[start], lists[end])
                start += 1
                end -= 1

            # everything has now come been merged into lists[0]
            return lists[0]

        k = len(lists)

        return iterateLists(lists, k)
