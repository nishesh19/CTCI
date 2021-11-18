from collections import defaultdict


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = self._trie()

    def _trie(self):
        return defaultdict(self._trie)

    def addWord(self, key, val):
        curr_value = self.findWord(key)
        # Update existing values
        val -= curr_value

        curr = self.trie

        for k in key:
            curr = curr[k]

            if 'value' not in curr:
                curr['value'] = 0

            curr['value'] += val

        curr.setdefault('*')

    def prefixSum(self, prefix):
        curr = self.trie

        for p in prefix:
            if p not in curr:
                return 0
            curr = curr[p]

        if 'value' in curr:
            return curr['value']

        return 0

    def findWord(self, word):
        curr = self.trie

        for w in word:
            if w not in curr:
                return 0
            curr = curr[w]

        if '*' in curr:
            return curr['value']
        else:
            return 0

    def insert(self, key: str, val: int) -> None:
        self.addWord(key, val)

    def sum(self, prefix: str) -> int:
        return self.prefixSum(prefix)


if __name__ == '__main__':

    # Your MapSum object will be instantiated and called as such:

    obj = MapSum()
    obj.insert("a", 3)
    print(obj.sum('ap'))
    # obj.insert('app', 2)
    # obj.insert("apple", 4)
    # print(obj.sum('apple'))
