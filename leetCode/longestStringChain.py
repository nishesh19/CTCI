from collections import Counter


class Solution:
    def longestStrChain(self, words) -> int:
        words_len = len(words)
        chain = [None for _ in range(words_len)]
        max_chain = 0
        
        for i in range(words_len):
            curr_chain = 0
            for j in range(i):
                if self.isPredecessor(words[j], words[i]):
                    curr_chain = max(curr_chain, chain[j])
            chain[i] = 1 + curr_chain
            max_chain = max(max_chain, chain[i])

        return max_chain
        

    def isPredecessor(self, str1, str2):
        if len(str2) - len(str1) != 1:
            return False

        alreadyDiff = False

        i, j = 0, 0

        while (i < len(str1)) and (j < len(str2)):
            if str1[i] != str2[j]:
                if alreadyDiff:
                    return False
                alreadyDiff = True
                j += 1
            else:
                i += 1
                j += 1

        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]))
