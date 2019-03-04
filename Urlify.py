# Write a method to replace all spaces in a string with '%20: You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith "J 13
# Output: "Mr%20John%20Smith"

#!/bin/python3

import math
import os
import random
import re
import sys

def URLify(sentence):
    char_list = list(sentence.rstrip())
    for i in range(len(char_list)):
        if char_list[i] == " ":
            char_list[i] = "%20"

    print(''.join(char_list))
if __name__ == '__main__':
    URLify(str(input()))

