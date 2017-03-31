class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def isBST(root, min=float('-inf'), max=float('inf')):
            if not root:
                return True
            if root.val >= max or root.val <= min:
                return False
            return isBST(root.left, min, root.val) and isBST(root.right, root.val, max)

        def size(root):
            if not root:
                return 0
            return size(root.left) + 1 + size(root.right)

        if isBST(root):
            return size(root)

        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))