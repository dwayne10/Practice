class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import random

        def pivot(nums, p_index, p):
            '''
                p: pivot value
                p_index: pivot index
            '''
            nums[p_index], nums[-1] = nums[-1], nums[p_index]

            curr = 0
            j = 0 # index of the element that is smaller than pivot
            while curr != len(nums) - 1:
                if nums[curr] > p:
                    # only do swap when current value is > than p
                    # j is pointing to an element that is definitely lesser
                    # than p
                    nums[curr], nums[j] = nums[j], nums[curr]
                    j += 1

                # if the nums[curr] is lesser than p
                # we don't increment j
                curr += 1

            nums[j], nums[-1] = nums[-1], nums[j]

            return j

        def quickselect(nums, k, start, end):
            while start <= end:
                pivot_index = random.randint(start, len(nums) - 1)

                pivot_number = nums[pivot_index]
                pivot_size = pivot(nums, pivot_index, pivot_number)

                if pivot_size == k - 1:
                    return nums[pivot_size]

                elif pivot_size > k - 1:
                    nums = nums[start:pivot_size]
                    end = pivot_size - 1
                else:
                    nums = nums[pivot_size+1:]
                    k = k - pivot_size - 1
        if not nums:
            return
        if k > len(nums):
            return -1
        return quickselect(nums, k, 0, len(nums) - 1)

print(Solution().findKthLargest([3,2,1,5,6,4], 2))