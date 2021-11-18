from typing import List
from collections import defaultdict
from heapq import heappush,heappop
class Trie:
    def __init__(self):
        self.trie = self._trie()

    def _trie(self):
        return defaultdict(self._trie)

    def add_word(self,word):
        curr = self.trie

        for w in word:
            curr = curr[w]
            if 'word' not in curr:
                curr['word'] = []
            
            curr['word'].append(word)

        curr.setdefault('*')

    def insert_heap():
        pass
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        pass
    

    def input(self, c: str) -> List[str]:
        pass


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
trie = Trie()
trie.add_word('i love you')
trie.add_word('island')