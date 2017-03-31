class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        prevR = prevB = prevG = 0
        red = blue = green = 0
        for cost in costs:
            red = cost[0] + min(prevB, prevG)
            blue = cost[1] + min(prevR, prevG)
            green = cost[2] + min(prevR, prevB)

            prevR, prevB, prevG = red, blue, green

        return min(min(red, blue), green)


    