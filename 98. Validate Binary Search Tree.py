# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isBST(root, min, max):
            if not root:
                return True

            if root.val >= max or root.val <= min:
                return False

            return isBST(root.left, min, root.val) and isBST(root.right,
                                                             root.val, max)

        if not root:
            return True

        min = float('-inf')
        max = float('inf')
        return isBST(root, min, max)