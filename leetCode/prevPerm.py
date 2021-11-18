class Solution:
    def prevPermOpt1(self, A):
        if not A:
            return A
        
        index = None
        
        for i in reversed(range(len(A)-1)):
            if A[i] > A[i+1]:
                index = i
        
        if index is None:
            return A
        
        swap_index = index + 1
        
        for i in range(i+2,len(A)):
            if A[index] > A[i] > A[swap_index]:
                swap_index = i
                
        A[index],A[swap_index] = A[swap_index],A[index]
        
        return A
    

if __name__ == '__main__':
    sol = Solution()
    
    print(sol.prevPermOpt1([3,2,1]))