'''
1.6 String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
'''
import math
import os
import random
import re
import sys
from string import ascii_lowercase
from collections import Counter


def compressed(input_str):
    input_str = input_str.lower()
    input_len = len(input_str)
    compressed_str = ''
    compressed_str_len = 0
    previous_char = ''
    previous_char_count = 0
    for char in input_str:
        if previous_char != char:
            if previous_char_count != 0:
                compressed_str += str(previous_char_count)
                compressed_str_len += 1
            compressed_str += char
            compressed_str_len += 1
            if compressed_str_len > input_len:
                return False,None
            previous_char = char
            previous_char_count = 1
        else:
            previous_char_count += 1
    
    compressed_str += str(previous_char_count)
    compressed_str_len += 1

    return (True,compressed_str) if (compressed_str_len < input_len) else (False,None)

if __name__ == '__main__':
    orig_str = input()
    is_smaller , compressed_str = compressed(orig_str)
    
    print(compressed_str if is_smaller else orig_str)
    