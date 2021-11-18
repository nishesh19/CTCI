def binarySearch(nums,start,end,target):
        if end<start:
            return -1
        
        mid = start + (end-start)//2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return binarySearch(nums,start,mid-1,target)
        else:
            return binarySearch(nums,mid+1,end,target)
        

if __name__ == '__main__':
    print(binarySearch([7,7,8],0,3,8))