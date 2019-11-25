class Solution:
    def wiggleMaxLength(self, nums) -> int:
        nums_len = len(nums)
        diff = [nums[i]-nums[i-1] for i in range(1, nums_len)]
        length = [[0 for i in range(2)] for j in range(nums_len)]



        
