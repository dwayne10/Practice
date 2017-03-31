# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
            Perform BFS
            algo: maintain two queue's :
            1. One for the nodes's vals
            2. Other for the col number. Set the root node as col 0. Stuff to left of root node subtract 1
            Stuff to right of root node add 1 each time we see a right node

            Importantly, maintain a hash map from the col number to the nodes at that column number
        """
        if not root:
            return []

        from collections import defaultdict
        col_num_to_nodes_map = defaultdict(list)

        minimum = 0  # min col num i.e leftmost col #
        maximum = 0  # max col num i.e rightmost col #

        q = []
        cols = []
        q.append(root)
        cols.append(0)

        while len(q) >= 1:
            node = q.pop(0)
            col = cols.pop(0)

            col_num_to_nodes_map[col].append(node.val)

            if node.left:
                q.append(node.left)
                cols.append(col - 1)
                minimum = min(minimum, col - 1)

            if node.right:
                q.append(node.right)
                cols.append(col + 1)
                maximum = max(maximum, col + 1)

        res = []
        for c in range(minimum, maximum + 1):
            res.append(col_num_to_nodes_map[c])
        return res


