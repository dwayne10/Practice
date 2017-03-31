class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """

        def find_quad(x, a, b, c):
            # return the output of f(x) = ax2 + bx + c
            return a * x * x + b * x + c

        if not nums:
            return []
        res = [None] * len(nums)

        # if a >= 0:
        #   the shape of the graph is like a happy smiley. The max are on extreams of left and right
        #   with min being at the middle
        # so we compare the leftmost and rightmost items from nums and add the larger to the right side of the res list
        # the pointer in this case starts from rightmost side of res

        start = 0
        end = len(nums) - 1
        if a >= 0:  # in this case compare the left and right sides of num list. either of them will be the max
            # in this case we start writing from the end as they are the max's each time
            write_pointer = end

            while start <= end:
                left = find_quad(nums[start], a, b, c)
                right = find_quad(nums[end], a, b, c)

                if left > right:
                    res[write_pointer] = left
                    start += 1
                else:
                    res[write_pointer] = right
                    end -= 1
                write_pointer -= 1

        elif a < 0:
            # sad smiley shape. The max lies at the middle
            # min lies at the extremes. so start with write_pointer at index 0
            # in this case compare the left and right sides of num list. either of them will be the min
            # so start feeding in the res from the index 0

            write_pointer = 0
            while start <= end:
                left = find_quad(nums[start], a, b, c)
                right = find_quad(nums[end], a, b, c)

                if left < right:
                    res[write_pointer] = left
                    start += 1
                else:
                    res[write_pointer] = right
                    end -= 1
                write_pointer += 1

        return res