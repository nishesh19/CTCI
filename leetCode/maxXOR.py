from collections import defaultdict
class Trie():
    def __init__(self):
        self._trie = self.trie()
        
    def trie(self):
        return defaultdict(self.trie)
    
    def insert(self,bits):
        curr = self._trie
        for bit in bits:
            curr = curr[bit]
        
        curr['value'] = int(bits,2)            
        curr.setdefault('*')
        
    def search(self,bits):
        curr = self._trie
        for bit in bits:
            if (bit == '1') and ('0' in curr):
                curr = curr['0']
            elif (bit == '0') and ('1' in curr):
                curr = curr['1']
            else:
                curr = curr[bit]
                
        return int(bits,2) ^ curr['value']

class Solution:
    def findMaximumXOR(self, nums) -> int:
        trie = Trie()
        max_xor = 0
        max_bits = len(bin(max(nums))[2:])
        for num in nums:
            num_bits = (bin(num)[2:]).zfill(max_bits)
            trie.insert(num_bits)
            max_xor = max(max_xor,trie.search(num_bits))
        
        return max_xor
    
if __name__ == '__main__':
    sol = Solution()
    nums = [3, 10, 5, 25, 2, 8]
    
    print(sol.findMaximumXOR(nums))
            
        