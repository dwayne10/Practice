class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root, longest, curr):
            if not root:
                return
            if root.left and root.val > root.left.val:
                helper(root.left, longest, curr + 1)
            elif root.left:
                longest = max(longest, curr)
                helper(root.left, longest, 0)

            if root.right and root.val > root.right.val:
                helper(root.right, longest, curr + 1)
            elif root.right:
                longest = max(longest, curr)
                helper(root.right, longest, 0)
            return longest
        longest = 0

        return helper(root, longest, 0)