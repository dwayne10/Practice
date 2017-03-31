class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def prettyprint(self, head):
        curr = head
        plist = []
        while curr is not None:
            plist.append(curr.val)
            curr = curr.next
        print(plist)



def reverseFromMtoN(head, m, n):
    if not head:
        return

    if m == n :
        return head

    dummy = ListNode(0)
    dummy.next = head
    pre = dummy

    i = 1
    while i <= m -1 :
        pre = pre.next
        i += 1

    start = pre.next
    tail = start.next

    diff = n - m
    while diff > 0:
        # swap in place
        start.next = tail.next
        tail.next = pre.next
        pre.next = tail
        tail = start.next
        pre.prettyprint(pre.next)
        diff -= 1

    dummy.prettyprint(dummy.next)
    return dummy.next




a = ListNode(5)
a.next = ListNode(6)
a.next.next = ListNode(9)
a.next.next.next = ListNode(10)
a.next.next.next.next = ListNode(4)
a.next.next.next.next.next = ListNode(7)
# a.next.next.next.next.next.next = ListNode(13)
a.prettyprint(a)
print("-----------------------")
reverseFromMtoN(a, 2, 6)