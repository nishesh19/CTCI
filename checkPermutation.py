# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.
#!/bin/python3

# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

import math
import os
import random
import re
import sys

def checkPermutation(input1,input2):
    if not input1 and not input2:
        return True
    elif not input1 or not input2:
        return False

    return ''.join(sorted(input1)) == ''.join(sorted(input2))


if __name__ == '__main__':
    print(checkPermutation(str(input()),str(input())))