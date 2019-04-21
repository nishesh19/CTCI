#!/bin/python3

# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

import math
import os
import random
import re
import sys

def isUnique(input_str):
    len_str = len(input_str)
    for i in range(len_str):
        for j in range(i+1,len_str):
            if input_str[i].lower() == input_str[j].lower():
                return False
    
    return True


if __name__ == '__main__':
    print(isUnique(str(input())))