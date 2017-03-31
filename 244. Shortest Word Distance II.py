class WordDistance(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        from collections import defaultdict
        # store the list of indexes of each word
        self.d = defaultdict(list)
        for index, word in enumerate(words):
            self.d[word].append(index)
            # print(self.d)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        indexes_of_word1 = self.d[word1]
        indexes_of_word2 = self.d[word2]
        index1 = index2 = 0
        diff = float('inf')
        while index1 < len(indexes_of_word1) and index2 < len(indexes_of_word2):
            diff = min(diff,
                       abs(indexes_of_word1[index1] - indexes_of_word2[index2]))
            if indexes_of_word1[index1] < indexes_of_word2[index2]:
                # move only index1 forward
                # logic here is we want two indexes to get as close to each other as possible
                # the two list indexes are sorted lists

                index1 += 1
            else:
                index2 += 1
        return diff


        # Your WordDistance object will be instantiated and called as such:
        # obj = WordDistance(words)
        # param_1 = obj.shortest(word1,word2)