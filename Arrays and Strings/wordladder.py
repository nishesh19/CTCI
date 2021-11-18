from collections import defaultdict
import math


class Trie:
    def __init__(self):
        self.trie = self._trie()

    def _trie(self):
        return defaultdict(self._trie)

    def insert(self, word):
        curr = self.trie

        for w in word:
            curr = curr[w]

        curr['word'] = word

    def find(self, word):
        return self.findOneDiffWord(self.trie, word, False)

    def findOneDiffWord(self, curr, word, isOneOff):
        if not word:
            return 0, None

        for i in range(len(word)):
            if word[i] not in curr:
                if isOneOff:
                    return math.inf, None

                min_hops = math.inf
                min_word = None
                for c in curr:
                    curr_steps, curr_word = self.findOneDiffWord(curr[c], word[i+1:], True)
                    if curr_steps < min_hops:
                        min_hops = curr_steps
                        min_word = curr_word

                return 1+min_hops, min_word
            else:
                curr = curr[word[i]]

        return 0,curr['word'] 


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList:
            return 0

        trie = Trie()

        for word in wordList:
            trie.insert(word)
 
        curr_word = beginWord
        total_steps = 0
        while curr_word != endWord:
            steps, curr_word = trie.find(curr_word)

            if steps == math.inf:
                return 0

            total_steps += steps

        return total_steps


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(Solution().ladderLength(beginWord, endWord, wordList))
