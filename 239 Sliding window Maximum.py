class Solution(object):

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        if k == 1:
            return nums
        from collections import deque
        res = []
        q = deque()
        i = 0
        maxi = float('-inf')
        while i < k:
            q.append(nums[i])
            if nums[i] > maxi:
                maxi = nums[i]
            i += 1

        res.append(maxi)

        for num in nums[i:]:
            last = q.popleft()
            if last == maxi:
                # need to recalculate max
                maxi = max(q)
                maxi = max(maxi, num)
                res.append(maxi)
                q.append(num)

            else:
                q.append(num)
                maxi = max(maxi, num)
                res.append(maxi)

        return res


class SolutionBest(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        from collections import deque

        res = []

        # deque for storing indexes of candidates
        dq = deque()

        for i in range(len(nums)):

            # remove index out of range k
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # remove smaller numbers in k range as they are useless
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # we are appending the index here
            dq.append(i)

            print(dq)
            if i >= k - 1:
                # dq[0] is the index of the max in the substring
                res.append(nums[dq[0]])

        return res

print(SolutionBest().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 4))


