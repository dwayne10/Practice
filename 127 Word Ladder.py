class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        def bfs(input, target, d, count):
            w = list(input)
            orig = list(input)

            for j in range(len(input)):
                for i in range(97, 123):
                    w[j] = chr(i)
                    new_word = ''.join(w)
                    if new_word == endWord:
                        return new_word, len(res) + 1
                    elif new_word in d:
                        res.append(new_word)
                        d.remove(new_word)
                        return new_word, 0
                    else:
                        w[j] = orig[j]  # reset the change
            return new_word

        res = []
        res.append(beginWord)
        d = set()
        for w in wordList:
            if w != beginWord:
                d.add(w)
        print(d)
        target = list(endWord)
        word = beginWord
        count = len(d)
        while len(d) > 0:
            word, done = bfs(word, target, d, count)
            if done:
                return done
        return 0

print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))