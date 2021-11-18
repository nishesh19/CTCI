def cyclic_sort(nums):
  # TODO: Write your code here
  for i in range(len(nums)):
      if nums[i]!=i+1:
          sw_id = nums[i]-1
          nums[i],nums[sw_id] = nums[sw_id],nums[i]
    

  return nums


if __name__ == "__main__":
    print(cyclic_sort([3, 1, 5, 4, 2]))