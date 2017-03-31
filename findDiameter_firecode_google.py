class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node

    def diameter(self,root):
        return self.diameter_helper(root,BinaryTree.Height())

    class Height:
        def __init__(self,h = 0):
            self.h = h

    def diameter_helper(self,root,height):
        # left_height : Height of left subtree
        # right_height : Height of right subtree
        left_height = BinaryTree.Height()
        right_height = BinaryTree.Height()
        if root == None:
            height.h = 0
            return 0

        # ldiameter  : diameter of left subtree
        # rdiameter  : Diameter of right subtree 
        # Get the heights of left and right subtrees in left height and right height
        # and store the returned values in ldiameter and rdiameter
 
        left_height.h += 1
        right_height.h += 1

        ldiameter = self.diameter_helper(root.left_child,left_height)
        rdiameter = self.diameter_helper(root.right_child,right_height)
        # Height of current node is max of heights of left and right subtrees plus 1
        height.h = max(left_height.h,right_height.h) + 1
        # diameter
        return max(left_height.h + right_height.h + 1, max(ldiameter,rdiameter))