class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def has_path_sum(root, sum):
    if not root:
        return False

    return has_path_sum_helper(root, sum)


def has_path_sum_helper(root, current_rem_sum):
    if not root:
        return False

    # If leaf node
    if not root.left and not root.right:
        return current_rem_sum - root.val == 0


    return has_path_sum_helper(root.left, current_rem_sum - root.val) \
           or \
           has_path_sum_helper(root.right, current_rem_sum - root.val)


root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(15)
root.right.right = TreeNode(10)
root.right.right.left = TreeNode(8)
root.left.left = TreeNode(12)
root.left.left.left = TreeNode(20)
root.left.right = TreeNode(21)

print(has_path_sum(root, 12))
