from urllib.parse import urlparse
class Solution:
    
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        if not haystack or len(needle) > len(haystack):
            return -1
        
        self.prime = 26
        target_hash = 0
        curr_hash = 0
        for i in range(len(needle)):
            target_hash += ord(needle[i])*(self.prime**i)
            curr_hash += ord(haystack[i])*(self.prime**i)
        
        
        for i in range(len(needle),len(haystack)):
            if curr_hash == target_hash:
                return i-len(needle)

            curr_hash = self.recomputeHash(haystack[i-len(needle)],haystack[i],curr_hash,len(needle)-1)
            
            
        return len(haystack)-len(needle) if curr_hash == target_hash else -1
        
        
    def recomputeHash(self,old,new,curr_hash,size):
        
        curr_hash -= ord(old)
        curr_hash //= self.prime
        curr_hash += ord(new)*(self.prime**size)
        
        return curr_hash
    

haystack = "ababcaababcaabc"
needle = "ababcaabc"

print(Solution().strStr(haystack,needle))