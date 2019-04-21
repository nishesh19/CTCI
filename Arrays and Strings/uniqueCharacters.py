#!/bin/python3

# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

import math
import os
import random
import re
import sys

def isUnique(input_str):
    if len(input_str) > 256:
        return False
    alphabets = [False]*256
    for char in input_str:
        if alphabets[ord(char.lower())]:
            return False 
        alphabets[ord(char.lower())] = True
    return True


if __name__ == '__main__':
    print(isUnique(str(input())))