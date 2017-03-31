class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        longest = 0
        maxi = 1
        d = {}
        s = list(s)
        for index, char in enumerate(s):

            if char in d:
                if d[char] < index - longest:
                    # the last occurrence of this does not
                    # occur in the current run of longest
                    longest += 1
                else:
                    # last occurrence did occur during this run
                    # so update the longest to reflect this
                    longest = index - d[char]
            else:
                longest += 1
            maxi = max(longest, maxi)
            d[char] = index
        return max(maxi, longest)
