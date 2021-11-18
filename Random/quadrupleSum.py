def search_quadruplets(arr, target):
  quadruplets = []
  # TODO: Write your code here
  arr.sort()
  for i in range(len(arr)-3):
    search_quad(arr,i,target-arr[i],quadruplets)

  return quadruplets


def search_quad(arr,i,target,quads):
  for j in range(i+1,len(arr)-1):
    right = len(arr) - 1
    revised_t = target - arr[j]
    left = j+1
    while left<right:
      curr_sum = arr[left] + arr[right]
      if curr_sum == revised_t:
        quads.append([arr[i],arr[j],arr[left],arr[right]])
        left += 1
        right -= 1
      elif curr_sum > revised_t:
        right -= 1
      else:
        left += 1
        
if __name__ == "__main__":
    print(search_quadruplets([2, 0, -1, 1, -2, 2],2))
      

  
