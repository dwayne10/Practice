class Solution2(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def divide(nums, start, end, smaller):
            if start > end:
                return 0
            if end - start <= 1:
                return 0

            mid = start + (end - start) // 2

            left = divide(nums, start, mid, smaller)
            right = divide(nums, mid, end, smaller)

            merge = mergeAndCount(start, mid, end, nums, smaller)

            return merge

        def mergeAndCount(s, mid, e, nums, smaller):
            res = []  # sorted list
            # smaller = []
            i = s
            j = mid

            while i < mid and j < e:
                if nums[i] > nums[j]:
                    smaller[i] += e - j
                    res.append(nums[i])
                    i += 1
                else:
                    res.append(nums[j])
                    j += 1
            if i != mid:
                res.extend(nums[i:mid])
            else:
                res.extend(nums[j:e])
            nums[s:e] = res

            return smaller

        smaller = [0] * len(nums)
        return divide(nums, 0, len(nums), smaller)


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def divide(enums, start, end, smaller):
            if start > end:
                return 0
            if end - start <= 1:
                return smaller

            mid = start + (end - start) // 2

            left = divide(enums, start, mid, smaller)
            right = divide(enums, mid, end, smaller)

            merge = mergeAndCount(start, mid, end, enums, smaller)

            return merge

        def mergeAndCount(s, mid, e, enums, smaller):
            res = []  # sorted list
            i = s
            j = mid
            # each obj in enums is a pair of index, value
            # so enums[i][1] is the value
            # index is critical to deciding which smaller index to increment

            while i < mid and j < e:

                if enums[i][1] > enums[j][1]:
                    smaller[enums[i][0]] += e - j
                    res.append(enums[i])
                    i += 1

                else:
                    res.append(enums[j])
                    j += 1

            if i != mid:
                res.extend(enums[i:mid])
            else:
                res.extend(enums[j:e])
            enums[s:e] = res

            return smaller

        smaller = [0] * len(nums)
        return divide(list(enumerate(nums)), 0, len(nums), smaller)

nums = [5,10,6,20,25,7]
print(Solution().countSmaller(nums))
