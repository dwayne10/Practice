class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mask = [0]*len(words)
        for i, word in enumerate(words):
            for c in word:
                mask[i]  = mask[i] | 1 << (ord(c) - ord('a'))
        max_product = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if (mask[i] & mask[j] == 0) and len(words[i]) * len(words[j]) > max_product:
                    max_product = len(words[i]) * len(words[j])

        return max_product


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return (self.getHeight(root)) >= 0

    def getHeight(self, root):
        if not root:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        if left < 0 or right < 0 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)