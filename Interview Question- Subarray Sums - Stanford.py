def subarraySums(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    dp = [[0] * len(nums) for _ in range(len(nums))]
    total = 0
    # subsequences of length = 1
    for i in range(len(nums)):
        dp[i][i] = nums[i]
        total += nums[i]

    for length in range(2, len(nums) + 1):
        for i in range(len(nums) - length + 1):
            j = i + length - 1  # index of last element

            dp[i][j] = dp[i][j - 1] + dp[j][j]
            total += dp[i][j]

    print(dp)
    print(total)
    return total

print(subarraySums([3, 10, 11, 2]))


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
