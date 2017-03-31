class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root, count, prev):
            if not root:
                return 1
            if root.val - prev == 1:
                count += 1
            else:
                count = 1
            left = dfs(root.left, count, root.val)
            # print(left)
            right = dfs(root.right, count, root.val)
            # print(right)
            return max(max(left, right), count)

        if not root:
            return 0
        return max(dfs(root.left, 1, root.val), dfs(root.right, 1, root.val))

a = TreeNode(1)
a.right = TreeNode(3)
a.right.left = TreeNode(2)
a.right.right = TreeNode(4)
a.right.right.right = TreeNode(5)
print(Solution().longestConsecutive(a))