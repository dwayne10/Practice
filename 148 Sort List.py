# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def find_mid(head):
            fast = head
            slow = head
            prev = head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            return slow

        def divideAndSort(h):
            if not h:
                return None
            if h.next is None:
                # Single length node
                return h
            mid = find_mid(h)
            h1 = divideAndSort(h)
            h2 = divideAndSort(mid)

            # if h1 or h2
            head = merge(h1, h2)
            return head

        def merge(h1, h2):

            curr = ListNode(0)
            dummy = curr

            while curr and h1 and h2:
                if h1.val < h2.val:
                    curr.next = h1
                    h1 = h1.next
                else:
                    curr.next = h2
                    h2 = h2.next
                curr = curr.next

            if h1:
                curr.next = h1
            else:
                curr.next = h2
            return dummy.next

        return divideAndSort(head)


a = ListNode(10)
a.next = ListNode(3)
a.next.next = ListNode(5)
a.next.next.next = ListNode(1)
a.next.next.next.next = ListNode(19)
a.next.next.next.next.next = ListNode(11)
a.next.next.next.next.next.next = ListNode(13)

print(Solution().sortList(a))