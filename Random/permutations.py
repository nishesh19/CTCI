from collections import deque
def find_permutations(nums):
  result = []
  q = deque([[]])
  num_len = len(nums)
  for num in nums:
    n = len(q)
    for i in range(n):
      curr = q.popleft()
      for i in range(len(curr)+1):
        temp = list(curr)
        temp.insert(i,num)
        if len(temp) == num_len:
          result.append(temp)
        else:
          q.append(temp)
  # TODO: Write your code here
  return result


def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
