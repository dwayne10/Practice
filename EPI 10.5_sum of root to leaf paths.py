class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sum_root_to_leaf_paths(root):

    so_far = ""
    total = sum_helper(root, so_far)

    return total


def sum_helper(root, so_far):

    # check if leaf
    if root and not root.left and not root.right:
        return int(so_far + str(root.val), 2)

    left = 0
    if root.left:
        left = sum_helper(root.left, so_far + str(root.val))

    right = 0
    if root.right:
        right = sum_helper(root.right, so_far + str(root.val))

    return left + right


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.right.right = TreeNode(1)
root.right.right.left = TreeNode(0)
root.left.left = TreeNode(1)
root.left.left.left = TreeNode(0)
root.left.right = TreeNode(1)
# root.left.left.left = TreeNode(7)
print(sum_root_to_leaf_paths(root))
