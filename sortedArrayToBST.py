class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return []
        root = TreeNode(nums[len(nums)//2])
        left = nums[:len(nums)//2]
        right = nums[len(nums)//2 + 1 :]
        if not left and not right:
            # base case when its a leaf node
            return root
        root.left = self.sortedArrayToBST(left) if left else None
        root.right = self.sortedArrayToBST(right) if right else None
        return root