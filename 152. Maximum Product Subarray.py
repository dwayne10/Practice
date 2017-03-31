class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxProduct = nums[0]
        minProduct = nums[0]
        maxOverall = nums[0]

        for num in nums[1:]:

            if num >= 0:
                maxProduct = max(maxProduct * num, num)
                minProduct = min(minProduct * num, num)

            else:
                # num < 0 - negative number

                temp = maxProduct
                maxProduct = max(minProduct * num,
                                 num)  # imagine min negative * -ve number
                minProduct = min(temp * num,
                                 num)  # this could be largest +ve number * -ve number
            maxOverall = max(maxOverall, maxProduct)
        return maxOverall