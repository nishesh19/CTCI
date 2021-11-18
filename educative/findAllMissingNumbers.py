def find_missing_numbers(nums):
  missingNumbers = []
  i = 0
  while i<len(nums):
    j = nums[i] - 1

    if j<len(nums) and nums[i]!= i + 1 and nums[i] != nums[j]:
      nums[i],nums[j] = nums[j],nums[i]
    else:
      i += 1

  for i in range(len(nums)):
    if nums[i] != i + 1:
      missingNumbers.append(i+1)
  # TODO: Write your code here
  return missingNumbers

if __name__ == "__main__":
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))


