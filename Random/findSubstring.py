from collections import Counter
import math


def find_substring(str, pattern):
    pat_count = Counter(pattern)
    start, end = 0, 0
    min_len = math.inf
    curr_len = 0
    matched = 0
    result = ''

    while (start < len(str)-len(pattern)+1):
        if end < len(str):    
            if str[end] in pat_count:
                pat_count[str[end]] -= 1

                if pat_count[str[end]] == 0:
                    matched += 1
              
        if matched == len(pattern):
            if end-start+1 < min_len:
                result = str[start:end+1]
                min_len = end-start+1

            if str[start] in pat_count:
                pat_count[str[start]] += 1
                if pat_count[str[start]] > 0:
                    matched -= 1

            curr_len -= 1
            start += 1
        
        
        
    # TODO: Write your code here
    return result


if __name__ == '__main__':
    print(find_substring('aabdec', 'abc'))
