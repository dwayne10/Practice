class Solution(object):

    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        def backtrack(str, i, pattern, j):
            # base cases
            if i == len(str) and j == len(pattern):
                # we are done
                return True
            if i == len(str) or j == len(pattern):
                return False

            if j < len(pattern) and pattern[j] in d:
                # pattern character exists in dictionary
                cache_string = d[pattern[j]]

                if cache_string == str[i: i + len(cache_string)]:
                    # if str's substring matches the dictionary
                    # move both pattern and str pattern forward
                    return backtrack(str, i + len(cache_string), pattern, j + 1)
                else:
                    # we need to backtrack
                    return False

            # if pattern not in d
            for k in range(i, len(str)):
                # this is the substring from i to k inclusive
                pat = str[i:k + 1]

                if pat in d.values():
                    # this is for the case when two elements
                    # of the pattern point to same substrings
                    # this should not happen
                    # eg: pattern "ab" and str "aa" should return False
                    continue

                d[pattern[j]] = pat
                if backtrack(str, k + 1, pattern, j + 1):
                    return True

                # backtrack
                d.pop(pattern[j])

            # nothing matched
            return False

        if not str and not pattern:
            return True
        if str and not pattern:
            return False
        d = {}
        return backtrack(str, 0, pattern, 0)


print(Solution().wordPatternMatch("abab", "redblueredblue"))


class Solution(object):

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        from collections import deque
        res = []
        q = deque()
        i = 0
        maxi = float('-inf')
        while i < k:
            q.append(nums[i])
            if nums[i] > maxi:
                maxi = nums[i]
            i += 1

        res.append(maxi)

        for num in nums[i:]:
            last = q.popleft()
            if last == maxi:
                # need to recalculate max
                maxi = max(q)
                maxi = max(maxi, num)
                res.append(maxi)
                q.append(num)

            else:
                q.append(num)
                maxi = max(maxi, num)
                res.append(maxi)

        return res


class Solution(object):

    def fractionToDecimal(self, num, den):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        rem = num % den

        if not rem:
            return str(num / den)

        else:
            div = str(num / den).split(".")
            decimal_part = div[1]
            integer_part = div[0]

            seen = []

            for n in decimal_part:
                if n not in seen:
                    seen.append(n)
                else:
                    break

            if integer_part:
                return integer_part + ".(" + ''.join(seen) + ")"
            else:
                return "0" + ".(" + str(''.join(seen)) + ")"
