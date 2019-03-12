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
from collections import Counter


def isOneAway(str1, str2):
    c1 = Counter(str1.lower())
    c2 = Counter(str2.lower())
    
    return sum((c1-c2).values()) == 1 if len(str1) >= len(str2) else sum((c2-c1).values()) == 1


if __name__ == '__main__':
    print(isOneAway(input(), input()))
