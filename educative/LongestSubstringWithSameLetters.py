from collections import defaultdict
def length_of_longest_substring(str, k):
  letters = defaultdict(int)
  start = 0
  max_len = 0
  curr_k = k
  for end in range(len(str)):
    letters[str[end]] += 1

    if str[end] != str[start]:
      if curr_k>0:
        curr_k -= 1
      else:
        while True:
          letters[str[start]] -= 1
          start += 1

          replacements = end - start + 1 - letters[str[start]]

          if replacements<=k:
            curr_k = k - replacements
            break
        
    max_len = max(max_len,end-start+1)
      
  return max_len


if __name__ == '__main__':
    print(length_of_longest_substring('aabccbb', 2))