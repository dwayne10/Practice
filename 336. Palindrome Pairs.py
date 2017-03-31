class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        lookup = {}
        for i, word in enumerate(words):
            lookup[word] = i

        for i in range(len(words)):
            for j in range(len(words[i]) + 1):
                prefix = words[i][:j]
                suffix = words[i][j:]
                rev_suffix = suffix[::-1]
                rev_prefix = prefix[::-1]

                if suffix == rev_suffix and rev_prefix in lookup and lookup[rev_prefix] != i:
                    res.append([i, lookup[rev_prefix]])

                if j > 0 and prefix == rev_prefix and rev_suffix in lookup and lookup[rev_suffix] != i:
                    # Eg: word = "lls" , prefix = "ll", suffix = "s" and rev_suffix is "s" which is at index 3
                    # So append[ 3, 2] which is "s" + "lls" which makes a palindrome
                    res.append([lookup[rev_suffix], i])
        return res


print(Solution().palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))