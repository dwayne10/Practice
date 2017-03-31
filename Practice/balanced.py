
def isBalanced(root):

	return isBalancedHelper(root) >= 1 

	def isBalancedHelper(root):
		if not root:
			return 0

		leftHeight = isBalancedHelper(root.left)
		rightHeight = isBalancedHelper(root.right)

		if leftHeight < 0 or rightHeight < 0 or abs(leftHeight - rightHeight) >= 1:
			return -1 

		return 1 + max(leftHeight,rightHeight)