class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(start, end, longest):
            if start > end:
                return -1

            if s[start] == s[end]:
                longest += 1
                start += 1
                end -= 1
                helper(start, end, longest)

            else:
                return (max(helper(start, end - 1, longest), helper(start + 1, end, longest)))

            return longest

        return helper(0, len(s) - 1, 0)
