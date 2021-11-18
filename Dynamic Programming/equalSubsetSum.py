'''
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.

Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}

Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}
'''

def can_partition(nums):
  if not nums:
      return False
  
  s = sum(nums)
  
  if s%2 != 0:
      return False
  
  dp = [[False for _ in range((s//2) + 1)] for _ in range(len(nums))]
  
  
  for i in range(len(nums)):
      dp[i][0] = True
      
  for i in range(1,(s//2) + 1):
      dp[0][i] = True if nums[0] == i else False
      
  for i in range(1,len(nums)):
      for j in range(1,(s//2) + 1):
          including = dp[i-1][j-nums[i]] if j>= nums[i] else False
          excluding = dp[i-1][j]
          
          dp[i][j] = including or excluding
          
  
  return dp[len(nums)-1][s//2]
  
def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()