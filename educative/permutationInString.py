from collections import Counter


def find_permutation(str, pattern):
    pat_len = len(pattern)
    pat_count = Counter(pattern)
    matched, start = 0, 0

    for end in range(len(str)):
        if str[end] in pat_count:
            pat_count[str[end]] -= 1

            if pat_count[str[end]] == 0:
                matched += 1

        if matched == len(pat_count):
            return True

        if end-start+1 >= pat_len:

            if str[start] in pat_count:

                if pat_count[str[start]] + 1 > 0:
                    matched -= 1

                pat_count[str[start]] += 1
            
            start += 1

    # TODO: Write your code here
    return False


if __name__ == '__main__':
    print(find_permutation('bcdxabcdy', 'bcdyabcdx'))
