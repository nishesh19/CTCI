def backspace_compare(str1, str2):
  # TODO: Write your code here
  if (not str1) or (not str2):
    return False
  
  i,j = len(str1)-1,len(str2)-1
  back1,back2 = 0,0
  while i>=0 and j>=0:
    while str1[i] == '#':
      back1 += 1
      i-=1

    while str2[j] == '#':
      back2 += 1
      j-=1

    i -= back1
    j -= back2
    if i<0 or j<0:
      break

    if str1[i] != str2[j]:
      return False

    i-=1
    j-=1

    

  return i<0 and j<0

def main():
  print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
  print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()
