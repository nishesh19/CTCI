def find_target_subsets(num, s):
  # TODO: Write your code here 
  dp = {}
  return find_targets_recur(num,dp,0,s)

def find_targets_recur(num,dp,index,s):
  if index == len(num):
    return 1 if s == 0 else 0
  
  key = str(index) + '-' + str(s)

  if key not in dp:
    add = find_targets_recur(num,dp,index+1,s+num[index])
    sub = find_targets_recur(num,dp,index+1,s-num[index])
    dp[key] = add + sub

  return dp[key]


def main():
  print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
  print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()