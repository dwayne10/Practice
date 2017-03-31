class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def delete(s, t, length, tlength):
            i = 0
            j = 0
            differ = 0
            while i < length and j < tlength:
                if s[i] != t[j]:
                    differ += 1
                    j += 1
                    if differ > 1:
                        return False
                else:
                    i += 1
                    j += 1
            return True

        def replace(s, t, length):
            i = 0
            differ = 0
            while i < length:
                if s[i] != t[i]:
                    differ += 1
                if differ > 1:
                    return False
                i += 1
            return differ == 1

        source_length = len(s)
        target_length = len(t)
        diff = abs(source_length - target_length)
        if diff > 1:
            return False
        elif diff == 0:
            # check replace
            return replace(s, t, source_length)
        else:
            # diff == 1
            # check delete or insert
            if source_length < target_length:
                return delete(s, t, source_length, target_length)
            elif source_length > target_length:
                # inverse it - this is for insert
                return delete(t, s, target_length, source_length)
        return False
