from heapq import heappush
from collections import defaultdict


def rearrange_string(str):
    char_freq = defaultdict(int)

    for char in str:
        char_freq[char] += 1

    char_count = []
    distinct_chars = 0
    for key in char_freq:
        if char_freq[key] == 1:
            distinct_chars += 1
        else:
            heappush(char_count, (-char_freq[key], key))
    
    
    return ""


def main():
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aapa"))


main()
