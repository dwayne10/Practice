# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        left = root.left
        right = root.right

        root.left = None

        self.flatten(left)
        self.flatten(right)

        root.right = left
        curr = root
        while curr and curr.right != None:
            curr = curr.right
        curr.right = right

a = TreeNode(1)
a.right = TreeNode(16)
a.left = TreeNode(7)
a.left.left = TreeNode(3)
a.left.right = TreeNode(4)
a.left.left.left = TreeNode(10)
a.left.left.right = TreeNode(11)
a.left.left.right.left = TreeNode(13)
a.left.left.left.left = TreeNode(12)
print(Solution().flatten(a))
print(a)