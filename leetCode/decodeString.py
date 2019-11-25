class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        result = ''
        if not s:
            return ''

        chars = []

        for char in s:
            if char == ']':
                encoded = ''
                number = ''

                while chars and chars[-1] != '[':
                    encoded += chars.pop()

                chars.pop()

                while chars and (chars[-1] != '[') and (not chars[-1].isalpha()):
                    number += chars.pop()
                    
                decoded = int(number[::-1]) * encoded[::-1]
                chars.append(decoded)
            else:
                chars.append(char)

        for char in chars:
            result += char

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.decodeString('100[LeetCode]'))
