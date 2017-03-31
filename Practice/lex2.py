class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        def helper(current, n):
            if current > n:
                return
            res.append(current)
            if current * 10 <= n:
                helper(current * 10, n)

            for i in range(1, 10):
                    if current + i <=n :
                        helper(current * 10 + i, n)


        res = []
        for i in range(1, 10):
            helper(i, n)
        return res


print(Solution().lexicalOrder(1000))