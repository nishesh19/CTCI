'''
https://www.hackerrank.com/challenges/equal-stacks/problem
'''

#!/bin/python3

import os
import sys
import math

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    sh1 = sum(h1)
    sh2 = sum(h2)
    sh3 = sum(h3)

    while h1 and h2 and h3:
        if sh1 == sh2 == sh3:
            return sh1
        elif sh1 >= max(sh2,sh3):
            sh1 -= h1.pop(0)
        elif sh2 >= max(sh1,sh3):
            sh2 -= h2.pop(0)
        else:
            sh3 -= h3.pop(0)

    return 0

    

if __name__ == '__main__':
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'equalStacksInput.txt')
    
    lines = []
    
    with open(my_file) as f:
        lines = f.readlines()
        
    n1N2N3 = lines[0].rstrip().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, lines[1].rstrip().split()))

    h2 = list(map(int, lines[2].rstrip().split()))

    h3 = list(map(int, lines[3].rstrip().split()))

    result = equalStacks(h1, h2, h3)

    print(str(result) + '\n')
