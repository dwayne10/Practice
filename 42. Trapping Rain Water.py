class Solution(object):
    def trap(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        if not heights or len(heights) <= 2:
            return 0

        stack = []
        left_max_so_far = heights[0]

        overall = 0
        i = 0

        done = False
        last = None
        while i < len(heights) and not done:

            j = i + 1
            while j < len(heights) and heights[j] <= left_max_so_far:
                stack.append(heights[j])
                j += 1

            if j >= len(heights):
                done = True
                # its a falling trend from the last max to the end
                if len(stack) >= 1:
                    if heights[len(heights) - 1] < heights[len(heights) - 2]:
                        stack.pop()  # ignore last block
                        j -= 2
                    else:
                        j -= 1
                    if stack:
                        # This part is from EPI Pg 467
                        # I use this when there is a decreasing sequence from the last
                        # left_max_so_far. Refer EPI for the better implementation
                        right = heights[j]
                        j -= 1
                        while j > i:
                            if heights[j] > right:
                                right = heights[j]
                            else:
                                overall += right - heights[j]
                            j -= 1
                        return overall
                else:
                    return max(overall, 0)
            # the two maxes are at the same height
            vals = 0
            while len(stack) > 0:
                vals += stack.pop()

            # vals are the boxes between the two maxes
            width = max(j - i - 1, 0)
            height = min(left_max_so_far, heights[j])
            if height and width:
                overall += abs((height * width) - vals)
            i = j
            left_max_so_far = heights[j]
        return overall
print(Solution().trap([10,1,8,2,4,3]))
