class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        length = len(s)
        if length == 1:
            return s[0]

        # Bottom - up DP
        start = end = 0
        dp = [[False] * length for _ in range(length)]

        # Length 1 substring
        for i in range(length):
            dp[i][i] = True

        # Length 2 substring
        for i in range(length - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                end = i + 1

        # substring Length 3 and above - upto len of string

        for l in range(3, length + 1):  # length of substring
            for i in range(length - l + 1):  # start index of substring
                j = i + l - 1  # end index of subtring
                # eg i=0 , l = 3, j = 0+3-1 = 2 so its 0->2
                if s[i] == s[j] and dp[i + 1][j - 1] == True:
                    dp[i][j] = True
                    start = i
                    end = j
        return s[start:end + 1]


