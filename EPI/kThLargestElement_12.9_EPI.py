import random

def kThSmallestElement(nums, k, left, right):
    def partition(nums, k, index, l, r):
        '''
        move elements less than pivot to its left
        elements > pivot to the right
        O(n)
        :return:
        '''
        pivot_value = nums[index]
        # swap pivot value and last value
        nums[index], nums[r] = nums[r], nums[index]
        j = l

        for curr in range(l,r):
            if nums[curr] < pivot_value:
                nums[j], nums[curr] = nums[curr], nums[j]
                j += 1

        nums[r], nums[j] = nums[j], nums[r]
        return j
    while left <= right:
        pivot = random.randint(left, right)
        r = partition(nums, k, pivot, left, right)
        if r == k-1:
            # found it
            return nums[r]
        elif r > k-1:
            # continue partition of left side
            right = r-1
        else:
            # continue partition of right side
            left = r+1

arr = [4,1,7,2,5,-1,10,15]
print(kThSmallestElement(arr, 1, 0, len(arr) -1))