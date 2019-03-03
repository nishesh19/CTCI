#!/bin/python3

# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

import math
import os
import random
import re
import sys

def isUnique(input_str):
    alphabets = [0]*26
    for char in input_str:
        if alphabets[ord(char.lower())-ord('a')] > 0:
            return False 
        alphabets[ord(char.lower())-ord('a')] += 1
    return True


if __name__ == '__main__':
    print(isUnique(str(input())))