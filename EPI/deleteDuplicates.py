'''
Write a program which takes as input a sorted array and updates it so that after all duplicates
have been removed and the remaning elements have been shifted left to fill the emptied indices
<2,3,5,5,7,11,11,11,13> => <2,3,5,7,11,13,0,0,0>
'''


def deleteDuplicates(A, key):
    value = A[key]
    vacant = 0

    for i in range(1, len(A)):
        if A[i] != value:
            vacant += 1
            A[vacant] = A[i]

    return vacant + 1


A = [int(x) for x in input().split(',')]
index = int(input)
print(deleteDuplicates(A, index))
print(A)
