class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums) <= 2:
            return max(nums)

        one = two = three = float('-inf')
        # instead of float('-inf') we can use null too
        for num in nums:
            if num in (one, two, three):  # we want only distinct numbers
                continue
            if num > one:
                one, two, three = num, one, two
            elif num > two:
                two, three = num, two
            elif num > three:
                three = num

        # if three is -inf there is no third max so return max(nums)
        return three if three != float('-inf') else max(nums)