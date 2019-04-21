'''
1.9 String Rotation: Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
'''
import numpy as np

def isSubstring(s1,s2):
    return s1 in s2


if __name__ == '__main__':
    str1 = input()
    str2 = input()

    print(isSubstring(str1,str2*2))