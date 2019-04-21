# 1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, pIe -> true
# pales. pale -> true
# pale. bale -> true
# pale. bake -> false

#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase
from difflib import ndiff

def isOneAway(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    addition = 0
    subtraction = 0
    
    for i,s in enumerate(ndiff(str1,str2)):
        if s[0] == '-':
            subtraction += 1
        elif s[0] == '+':
            addition += 1
    
    # One char was inserted or removed
    if (addition + subtraction) == 1:
        return True     
    # One char was replaced
    elif addition == subtraction == 1:
        return True
    else:
        return False

if __name__ == '__main__':
    print(isOneAway(input(),input()))