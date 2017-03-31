class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def createDPtable(s):
            table = [[False] * len(s) for _ in range(len(s))]

            for i in range(len(s)):
                if s[i] != '0':
                    table[i][i] = True

            # length 2
            for i in range(len(s) - 1):
                substring = s[i:i + 2]
                if substring[0] != '0' and int(substring) >= 1 and int(substring) <= 26:
                    table[i][i + 1] = True

            return table

        def backtrack(s, start, count):
            if start == len(s):
                count += 1
                return count

            for i in range(start, len(s)):
                if i - start <= 1 and dp[start][i]:
                    count = backtrack(s, i + 1, count)
            return count

        if not s:
            return 0

        dp = createDPtable(s)
        count = backtrack(s, 0, 0)
        return count

print(Solution().numDecodings("2324"))


class Solution2(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def numDecodingsHelper(s, cache):

            if len(s) == 0:
                return 1

            if cache[len(s)]:
                return cache[len(s)]

            # not in cache, so calculate by summing the tails
            sum = 0

            for headsize in range(1, len(s) + 1):
                head = s[:headsize]
                tail = s[headsize:]

                if int(head) > 26 or head[0] == "0":
                    break

                sum += numDecodingsHelper(tail, cache)

            cache[len(s)] = sum
            print(cache)
            return sum

        if not s:
            return 0
        return numDecodingsHelper(s, [0] * (len(s) + 1))


print(Solution2().numDecodings("23242221"))


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        ways = [0] * (len(s) + 1)

        # base cases

        ways[-1] = 1
        ways[-2] = 1 if s[-1] != '0' else 0

        # Very similar to fibonacci

        for i in range(len(s) - 2, -1, -1):
            if s[i] == '0':
                continue
            if int(s[i:i + 2]) <= 26:
                ways[i] = ways[i + 1] + ways[i + 2]
            else:
                ways[i] = ways[i + 1]

        return ways[0]



