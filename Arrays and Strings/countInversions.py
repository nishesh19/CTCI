from typing import List
from collections import deque
def optimizing_box_weights(arr: List[int]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE

    arr.sort(reverse=True)
    half = sum(arr)//2
    
    curr_sum = 0
    result = deque([])
    for i in range(len(arr)):
        curr_sum += arr[i]
        result.appendleft(arr[i])

        if curr_sum > half:
            break

    return result



nums = [1, 2, 3, 5, 8]
print(optimizing_box_weights(nums))
