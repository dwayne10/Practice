class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        i = 0
        j = len(s) - 1
        s = s.lower()

        while i <= j:

            if s[i] == ' ' or ord(s[i]) not in range(97, 123) and not s[i].isdigit():
                i += 1
            elif s[j] == ' ' or ord(s[j]) not in range(97, 123) and not s[j].isdigit():
                j -= 1

            elif s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1

        return True