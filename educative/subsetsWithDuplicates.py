def find_subsets(nums):
  if not nums:
    return [[]]

  nums.sort()  
  subsets = []
  subsets.append([])
  
  for i in range(len(nums)):
    start = 0

    if i-1 >=0 and nums[i-1] == nums[i]:
      start = 2**(i-1)
    
    end = len(subsets)
    for j in range(start,end):
      new_set = list(subsets[j])
      new_set.append(nums[i])

      subsets.append(new_set)
  

  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
