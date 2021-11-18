from collections import defaultdict
from heapq import heappush, heappop, heapify


def find_maximum_distinct_elements(nums, k):
    num_freq = defaultdict(int)
    count_heap = []
    for num in nums:
        num_freq[num] += 1

    distinct_num = 0
    for key in num_freq:
        if num_freq[key] == 1:
            distinct_num += 1
        else:
            heappush(count_heap, (num_freq[key], key))

    while count_heap and k > 0:
        curr_num = heappop(count_heap)

        if curr_num[0] - 1 != 1:
            heappush(count_heap, (curr_num[0]-1, curr_num[1]))
        else:
            distinct_num += 1
            
        k -= 1

    distinct_num -= k
    return distinct_num + sum([1 for x in count_heap if x[0] == 1])


def main():

    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()
