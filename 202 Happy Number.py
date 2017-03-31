class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        notHappy = True
        nums = list(str(n))
        seen = []
        total = 0
        while notHappy:
            nums = [pow(int(x), 2) for x in nums]
            total = sum(nums)
            if total == 1:
                return True
            if total not in seen:
                seen.append(total)
            else:
                return False
            nums = list(str(total))

