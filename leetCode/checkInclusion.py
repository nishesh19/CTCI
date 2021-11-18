from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s = len(s1)
        counter = Counter(s1)
        
        start = 0
        matched = 0
        
        for end in range(len(s2)):
            if s2[end] in counter:
                counter[s2[end]] -= 1
                
                if counter[s2[end]] == 0:
                    matched += 1
                
            if matched == len(counter):
                return True
            
            if end + 1 >= len_s:
                if s2[start] in counter:
                    if counter[s2[start]] ==0:
                        matched -= 1
                        
                    counter[s2[start]] += 1
                    
                start += 1
        
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkInclusion("trinitrophenylmethylnitramine","dinitrophenylhydrazinetrinitrophenylmethylnitramine"))