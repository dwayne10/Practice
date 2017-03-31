class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return

        start = 0
        end = len(height) - 1
        maxi = 0
        while end - start >= 1:
            if height[start] > height[end]:
                area = (end - start) * height[end]
                end -= 1
            else:
                area = (end - start) * height[start]
                start += 1
            maxi = max(area, maxi)

        return maxi
