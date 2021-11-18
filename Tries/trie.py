from collections import defaultdict


class Trie():
    def __init__(self):
        self.trie = self._trie()

    def _trie(self):
        return defaultdict(self._trie)

    def addWord(self, word):
        curr = self.trie
        for w in word:
            curr = curr[w]

        curr['word'] = word
        curr.setdefault('*')

    def removeWord(self, word):
        if not self.findWord(word):
            print("Word dosen't exist")

        del self.trie[word[0]]

    def findWord(self, word) -> bool:
        return self.findWildCardWord(word,self.trie)

    def findWildCardWord(self,word,trie):
        if not trie:
            return False
        i = 0
        while i<len(word):
            if word[i] == '.':
                for char in trie:
                    if self.findWildCardWord(word[i+1:],trie[char]):
                        return True
                return False
            else:
                if word[i] not in trie:
                    return False
                trie = trie[word[i]]
                i += 1
        
        return True if (trie and ('*' in trie)) else False


if __name__ == '__main__':
    trie = Trie()

    trie.addWord('hot')
    trie.addWord('jot')

    
    print(trie.findWord('.'))
    print(trie.findWord('a'))
    print(trie.findWord('aa'))
    print(trie.findWord('.a'))
    print(trie.findWord('a.'))
    
