class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.orig = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.orig

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        copy = self.orig[:]
        import random
        for i in range(len(copy) - 1, 0, -1):
            j = random.randint(0, i)

            # swap item at i and j
            copy[i], copy[j] = copy[j], copy[i]

        return copy
