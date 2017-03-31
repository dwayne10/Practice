# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def preOrderHelper(pre_start, pre_end, in_start, in_end):
            if pre_start >= pre_end or in_start >= in_end:
                return None

            root_index_inorder = in_map[preorder[pre_start]]
            left_subtree_size = root_index_inorder - in_start

            root = TreeNode(preorder[pre_start])
            # print(root.val)
            root.left = preOrderHelper(pre_start + 1, pre_start + 1 + left_subtree_size , in_start, root_index_inorder)
            root.right = preOrderHelper(pre_start + 1 + left_subtree_size, pre_end, root_index_inorder + 1, in_end)

            return root

        in_map = {}

        for index, val in enumerate(inorder):
            in_map[val] = index
            # print(in_map)
        return preOrderHelper(0, len(preorder), 0, len(inorder))


print(Solution().buildTree([10,6,12,4,9,3,15,13,17], [4,12,6,9,3,10,13,15,17]))

