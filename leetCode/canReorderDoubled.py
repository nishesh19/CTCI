from collections import Counter
class Solution:
    def canReorderDoubled(self, A) -> bool:
        if not A:
            return True
        
        A.sort()
        
        A_count = Counter(A)
        
        i,j = 0,0
        
        while (i < int(len(A)/2)) and (j<len(A)):
            if not A_count[A[j]]:
                j += 1
                continue
            
            A_count[A[j]] -= 1
            
            if A[j] < 0:
                if (int(A[j]/2) not in A_count) or (not A_count[int(A[j]/2)]):
                    return False
                
                A_count[int(A[j]/2)] -= 1
            else:
                if (2*A[j] not in A_count) or (not A_count[2*A[j]]):
                    return False
            
                A_count[2*A[j]] -= 1
            
            j +=1
            i += 1
            
        return True
    
    
if __name__ == '__main__':
    sol = Solution()
    A = [4,2,4,4,2,-4,0,-2,0,4]
    
    sol.canReorderDoubled(A)
                