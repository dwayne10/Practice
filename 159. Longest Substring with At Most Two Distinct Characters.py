class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) <= 2:
            return len(s)

        charsInRun = set()
        curr = 0
        longest = 0
        for index, char in enumerate(s):
            if char not in charsInRun and len(charsInRun) < 2:
                charsInRun.add(char)
                curr += 1
            elif char in charsInRun and len(charsInRun) <= 2:
                # increase curr length
                curr += 1
            elif char not in charsInRun and len(charsInRun) == 2:
                longest = max(longest, curr)
                curr = 2
                charsInRun = set()
                charsInRun.add(char)
                charsInRun.add(s[index - 1])
                i = index - 1
                while i > 0 and s[i] == s[i - 1]:
                    # add to curr value to track repetitions of prev character
                    curr += 1
                    i -= 1

        return max(longest, curr)
