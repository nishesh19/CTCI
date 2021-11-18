def search_triplets(arr):
  arr.sort()

  triplets = []
  # TODO: Write your code here

  for i in range(len(arr)):
    find_triplets(arr,i+1,triplets,-arr[i])
  return triplets

def find_triplets(arr,start,triplets,target):
  end = len(arr) - 1

  while start<end:
    curr_sum = arr[start] + arr[end]

    if curr_sum == target:
      triplets.append([arr[start],-target,arr[end]])
      start += 1
      end -= 1
    elif curr_sum > target:
      end -= 1
    else:
      start += 1


if __name__ == '__main__':
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))