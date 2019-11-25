from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, A, S: int) -> int:
        currSum = 0
        total_count = 0
        
        prefixSum = defaultdict(lambda:0)
        for i in range(len(A)):
            currSum += A[i]
            if currSum == S:
                total_count += 1
            if (currSum - S) in prefixSum:
                total_count += prefixSum[currSum - S]
                
            prefixSum[currSum] += 1
        
        return total_count
        
if __name__ == '__main__':
    sol = Solution()
    A = [0,0,0,0,0]
    S = 0
    print(sol.numSubarraysWithSum(A,S))
        
        