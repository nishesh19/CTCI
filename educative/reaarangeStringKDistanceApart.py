from collections import defaultdict
from heapq import heappush, heappop


def reorganize_string(str, k):
    char_freq = defaultdict(int)
    for char in str:
        char_freq[char] += 1

    max_heap = []
    for key in char_freq:
        heappush(max_heap, (-char_freq[key], key))

    second_max_heap = []
    result = ''
    curr_k = k
    while max_heap:
        curr_elem = heappop(max_heap)
        result += curr_elem[1]
        curr_k -= 1

        if curr_elem[0] + 1 !=0:
            heappush(second_max_heap, (curr_elem[0] + 1, curr_elem[1]))
        
        if curr_k == 0:
            if second_max_heap:
                heappush(max_heap,heappop(second_max_heap))
            
            curr_k = k
    return result


def main():
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Reorganized string: " + reorganize_string("Programming", 3))
    print("Reorganized string: " + reorganize_string("aab", 2))
    print("Reorganized string: " + reorganize_string("aapa", 3))


main()
