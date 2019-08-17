
#!/bin/python3

# 1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat". "atco cta". etc.)

import math
import os
import random
import re
import sys
from collections import Counter
from string import ascii_lowercase

def palindromePermutation(word):
    word = word.replace(" ","").lower()
    char_count = Counter(word)
    already_seen_single_count = False
    word_len = len(word)
    for alphabet in ascii_lowercase:
        if (char_count[alphabet] % 2) != 0:
            if (word_len % 2) == 0:
                # For even length word , there can't be odd count character in it for it to be a palindrome
                return False
            if already_seen_single_count:
                # For Odd lenght paldinrome word there can't be more than one single count characters
                return False
            already_seen_single_count = True
    return True


if __name__ == '__main__':
    print(palindromePermutation(input()))