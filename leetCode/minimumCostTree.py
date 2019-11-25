import sys
class Solution:
    def mctFromLeafValues(self, arr) -> int:
        min_product = sys.maxsize
        curr_product = 0
        for i in range(1,len(arr)):
            curr_product = self.treeCost(arr[i:]) * self.treeCost(arr[:i])
            
            min_product = curr_product if curr_product < min_product else min_product
            
            
    def treeCost(self,arr):
        if len(arr) == 1:
            return arr[0]
        
        mid = len(arr) // 2
        
        return self.treeCost(arr[:mid]) * self.treeCost(arr[mid:])
    

if __name__ == '__main__':
    sol = Solution()
    arr = [6,2,4]
    
    print(sol.mctFromLeafValues(arr))