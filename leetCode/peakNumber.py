import math

class Solution:
    def findPeakElement(self, nums) -> int:
        nums.append(-math.inf)
        nums.insert(0,-math.inf)
        
        return self.findPeak(nums,0,len(nums)) - 1
        
    def findPeak(self,nums,start,end):
        if end<=start:
            return -1
        
        mid = start + (end-start)//2
        
        if nums[mid-1] < nums[mid] > nums[mid + 1]:
            return mid
        
        left = self.findPeak(nums,start,mid)
        
        if left != -1:
            return left
        
        return self.findPeak(nums,mid+1,end)
    
    
if __name__ == '__main__':
    sol = Solution()
    
    print(sol.findPeakElement([1,2,3]))
        