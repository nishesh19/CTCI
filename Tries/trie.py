from collections import defaultdict

class Trie():
    def __init__(self):
        self.trie = self._trie()

    def _trie(self):
        return defaultdict(self._trie)

    def addWord(self, word):
        if self.findWord(word):
            print('Word already exists')
            return
        curr = self.trie
        for w in word:
            curr = curr[w]
        curr.setdefault('*')

    def removeWord(self, word):
        if not self.findWord(word):
            print("Word dosen't exist")
        
        del self.trie[word[0]]

    def findWord(self, word)->bool:
        curr = self.trie
        for w in word:
            if w not in curr:
                return False
            curr = curr[w]

        if '*' in curr:
            return True
        else:
            return False


if __name__ == '__main__':
    trie = Trie()
    
    words = ['cat','dog']
    
    for w in words:
        trie.addWord(w)

    trie.removeWord('cat')
    
    for w in words:
        print(trie.findWord(w))

    print(trie)