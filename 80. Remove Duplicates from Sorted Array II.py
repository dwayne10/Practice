class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        if len(nums) <= 2:
            return len(nums)
        i = 1
        j = 1
        count = 1
        while j < len(nums):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                count = 1  # tracks count of number at index j. Since its a new number reset count to 1
                i += 1
            else:
                if count < 2:
                    count += 1
                    nums[i] = nums[j]
                    i += 1
                else:
                    pass
                    # do nothing. i.e do not increment i
                    # this means the element at i is a duplicate
                    # wait till you a reach a new number and then overwrite that over this
            j += 1

        return i


print(Solution().removeDuplicates([1,1,2]))