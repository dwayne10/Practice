class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # Turn nums into a set of nums
        nums = set(nums)
        longest = 1

        for n in nums:
            # look if the previous number is in the nums
            # start the counting only for the lowest number of the subseq

            if n - 1 not in nums:
                y = n + 1 # next number in subseq
                while y in nums:
                    y += 1

                longest = max(longest, y - n)

        return longest
