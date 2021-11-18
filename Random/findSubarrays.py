def find_subarrays(arr, target):
  result = []
  # TODO: Write your code here
  
  for i in range(len(arr)):
    find_products(arr,target,i,result)

  return result

def find_products(arr,target,i,result):
  curr_prod = 1
  curr_lst = []

  while i<len(arr):
    if curr_prod * arr[i] >= target:
      break

    curr_lst.append(arr[i])
    result.append(curr_lst[:])
    curr_prod *= arr[i]
    i+=1



if __name__ == "__main__":
    print(find_subarrays([2, 5, 3, 10],30))