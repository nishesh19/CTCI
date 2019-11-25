'''
    Write a program which takes an array of n integers where A[i] denotes the maximum you
    can advance from index i,and returns whether it is possible to advance to the last
    index starting from the begining of the array.
    
    Variant: Compute the Minimum number of steps needed to advance to the last location
'''

import sys


def canBeAdvanced(A, index):
    minSteps = sys.maxsize

    if index >= len(A) - 1:
        return True, 1

    haspath = False

    for i in reversed(range(1, A[index] + 1)):
        path = canBeAdvanced(A, index + i)
        if(path[0]):
            minSteps = min(minSteps, path[1])
            haspath = True

    return haspath, 1 + minSteps


A = [int(x) for x in input()]
path = canBeAdvanced(A, 0)
if path[0]:
    print(f'Can be advanced in {path[1] - 1} steps')
else:
    print('Can"t be advanced')
