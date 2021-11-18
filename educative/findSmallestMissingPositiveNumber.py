def find_first_missing_positive(nums):
  # TODO: Write your code here
  i = 0
  while i<len(nums):
    j = nums[i]
    if nums[i]!=i and j>=0 and j<len(nums):
      nums[i],nums[j] = nums[j],nums[i]
    else:
      i += 1

  for i in range(1,len(nums)):
    if nums[i] != i:
      return i
        

if __name__ == "__main__":
    print(find_first_missing_positive([-3, 1, 5, 4, 2]))
