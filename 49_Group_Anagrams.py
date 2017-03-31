class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # key insight: anagrams will look the same when sorted
        d = {}
        for word in strs:
            w = ''.join(sorted(
                word))  # sort the letter of the word and join them together
            # w serves as a placeholder for the word

            if w not in d:
                d[w] = [word]
            else:
                d[w].append(word)
        return d.values()
