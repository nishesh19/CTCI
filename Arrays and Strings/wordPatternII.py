class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        return self.wordPatternMatchRecur(pattern, s, {}, set())

    def wordPatternMatchRecur(self, pattern, s, patToChar, seen):
        if not s and not pattern:
            return True

        if not s or not pattern:
            return False

        if pattern[0] in patToChar:
            if patToChar[pattern[0]] != s[:len(patToChar[pattern[0]])]:
                return False
            return self.wordPatternMatchRecur(pattern[1:], s[len(patToChar[pattern[0]]):], patToChar, seen)
        else:
            for i in range(len(s)):
                curr = s[:i+1]
                if curr not in seen:
                    patToChar[pattern[0]] = curr
                    seen.add(curr)

                    if self.wordPatternMatchRecur(pattern[1:], s[len(curr):], patToChar, seen):
                        return True

                    del patToChar[pattern[0]]
                    seen.remove(curr)

        return False


pattern = "d"
s = "e"
print(Solution().wordPatternMatch(pattern, s))
