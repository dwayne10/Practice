class Solution(object):

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        index_stack = []
        max_area = -1
        top_of_stack_index = 0
        area = 0

        i = 0
        while i < len(heights):
            if len(index_stack) == 0 or heights[i] >= heights[index_stack[-1]]:
                index_stack.append(i)
                i += 1
            else:
                # print(index_stack)
                top_of_stack_index = index_stack.pop()

                # calculate area after popping
                if len(index_stack) == 0:
                    area = heights[top_of_stack_index] * i
                else:
                    area = heights[top_of_stack_index] * (i - index_stack[-1] - 1)
                max_area = max(max_area, area)

        while len(index_stack) >= 1:

            top_of_stack_index = index_stack.pop()

            # calculate area after popping

            if len(index_stack) == 0:
                area = heights[top_of_stack_index] * i

            else:

                area = heights[top_of_stack_index] * (i - index_stack[-1] - 1)
            max_area = max(max_area, area)
        return max_area


