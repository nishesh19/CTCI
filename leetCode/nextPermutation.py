class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        index = None
        
        for i in reversed(range(len(nums)-1)):
            if nums[i] < nums[i+1]:
                index = i
                break
                
        if index is None:
            nums.sort()
            return
                
        swap_index = index + 1
        
        for i in range(index+2,len(nums)):
            if nums[index] < nums[i] <= nums[swap_index]:
                swap_index = i
                
        nums[index],nums[swap_index] = nums[swap_index],nums[index]
        
        nums[index+1:] = reversed(nums[index+1:])
        
        
if __name__ == '__main__':
    sol = Solution()
    nums = [2,3,1,3,3]
    sol.nextPermutation(nums)
    print(nums)    