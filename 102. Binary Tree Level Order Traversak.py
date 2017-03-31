# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = [[]]
        from collections import deque
        q = deque()
        q.append((root, 0))

        while q:

            node, level = q.popleft()

            if len(res) - 1 < level:
                res.append([node.val])
            else:
                res[level].append(node.val)

            if node.left:
                q.append((node.left, level + 1))

            if node.right:
                q.append((node.right, level + 1))

        return res



