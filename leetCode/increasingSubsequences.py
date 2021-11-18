class Solution:
    def findSubsequences(self, nums):
        incr_seq = set()
        nums_len = len(nums)
        
        for i in range(nums_len-1):
            for j in range(i+1,nums_len):
                for l in range(2,nums_len-i+1):
                    curr_seq = [nums[i]]
                    k = j
                    while (k<nums_len):
                        if nums[k] >= curr_seq[-1]:
                            curr_seq.append(nums[k])
                            k += 1
                            
                        if len(curr_seq) == l:
                            incr_seq.add(tuple(curr_seq))
                            break
                        
                            
        result = []                        
        for seq in incr_seq:
            result.append(list(seq))
            
        return result
    
if __name__ == '__main__':
    seq = [4, 6, 7, 7]
    
    sol = Solution()
    
    print(sol.findSubsequences(seq))