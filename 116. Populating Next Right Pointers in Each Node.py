# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing

    def connect(self, origroot):
        root = origroot
        leftmost = None
        while root:
            if root.left:
                if root == leftmost:
                    # store the next leftmost node
                    leftmost = root.left
                root.left.next = root.right

            if root.next:
                if root.right:
                    root.right.next = root.next.left
                root = root.next
            else:

                if not root.left and not root.right and root.next is None:
                    # reached rightmost leaf, we are done
                    break
                if not leftmost:
                    # at the root node
                    root = root.left
                    leftmost = root
                else:
                    root = leftmost

