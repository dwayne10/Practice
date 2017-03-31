class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        s = list(s)
        p = list(p)
        if not p:
            return False
        correct_pattern = p[0]
        # Very IMP - Merge mutiple * together
        i = 1
        while i < len(p):
            while i < len(p) and p[i] == p[i - 1] == "*":
                i += 1
            if i < len(p):
                correct_pattern += p[i]
                i += 1
        p = correct_pattern

        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # first row and first column are null strings
        # similar concept and reason to Edit Distance

        dp[0][0] = True  # as null string matches null

        if len(p) >= 1 and p[0] == "*":
            # Special Case
            # where * == null when  * is the first char of the pattern
            dp[0][1] = True

        # the row is the pattern
        # and the column is the string
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):

                if p[j - 1] == "?" or p[j - 1] == s[i - 1]:
                    # check cell diagonally
                    dp[i][j] = dp[i - 1][j - 1]

                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[len(dp) - 1][len(dp[0]) - 1]


