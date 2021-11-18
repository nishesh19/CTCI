class Solution:
    def searchRange(self, nums, target) :
        index = self.binarySearch(nums,0,len(nums)-1,target)
        
        if index == -1:
            return [-1,-1]
        
        lindex = self.searchLeft(nums,0,index,target)
        rindex = self.searchRight(nums,index,len(nums)-1,target)
        
        return [lindex,rindex]
    
    def binarySearch(self,nums,start,end,target):
        if end<start:
            return -1
        
        mid = start + (end-start)//2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binarySearch(nums,start,mid-1,target)
        else:
            return self.binarySearch(nums,mid+1,end,target)
        
        
    def searchLeft(self,nums,start,end,target):
        if end<=start:
            return end
        
        mid = start + (end-start)//2
        
        if nums[mid] == target:
            return self.searchLeft(nums,start,mid,target)
        
        index = self.binarySearch(nums,mid+1,end,target)
        
        return self.searchLeft(nums,mid+1,index,target)
    
    
    def searchRight(self,nums,start,end,target):
        if end<=start:
            return end if nums[end] == target else end - 1
        
        mid = start + (end-start)//2
        
        if nums[mid] == target: 
            return self.searchRight(nums,mid+1,end,target)
        
        index = self.binarySearch(nums,start,mid-1,target)
        
        if index == -1:
            return start - 1
        
        return self.searchRight(nums,index,mid-1,target)
    
    
if __name__ == '__main__':
    sol = Solution()
    nums = [5,7,7,8,8,10]
    # print(sol.searchRange([5,7,7,8,8,10],8))
    # print(sol.searchRight(nums,3,len(nums)-1,8))
    # print(sol.searchLeft(nums,0,len(nums)-1,8))
    print(sol.searchRange(nums,6))
