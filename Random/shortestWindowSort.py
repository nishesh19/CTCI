def shortest_window_sort(arr):
  # TODO: Write your code here
  left = 0
  right = len(arr) - 1

  while (left < len(arr) - 1) and (arr[left]<arr[left+1]):
    left += 1
  
  if left == right:
    return 0

  while (right >=1) and (arr[right] > arr[right-1]):
    right -= 1

  min_num = min(arr[left:right+1])
  max_num = max(arr[left:right+1])

  while (left >=1) and (arr[left-1] > min_num):
    left -= 1

  while (right<len(arr) - 1) and (arr[right+1] < max_num):
    right += 1


  return right - left + 1


if __name__ == '__main__':
    print(shortest_window_sort([1, 2, 3]))