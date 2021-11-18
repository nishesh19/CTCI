from collections import defaultdict 
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        result = []
        prefixSum = defaultdict(list)
        
        currSum = 0
        
        for j,num in enumerate(nums):
            currSum += num

            if currSum == k:
                result.append(nums[:j+1])
                
            if (currSum - k) in prefixSum:
                for i in prefixSum[currSum - k]:
                    result.append(nums[i+1:j+1])
                
            prefixSum[currSum].append(j)
            
            
        return result

nums = [2,-2,2,-2,2,3,-2]
k = 3
print (Solution().subarraySum(nums,k))