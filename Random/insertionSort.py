def insertionSort(A):
    for i in range(1, len(A)):
        while i > 0 and A[i] < A[i-1]:
            A[i], A[i-1] = A[i-1], A[i]
            i -= 1

A = [int(x) for x in input().split(',')]

insertionSort(A)

print(A)
