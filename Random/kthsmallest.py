def kthSmallest(A, k):
    if len(A) == 1:
        return A[0]
    
    pivot = A[-1]

    smaller = [x for x in A if x < pivot]
    larger = [x for x in A if x > pivot]

    if k == len(smaller) + 1:
        return pivot
    elif k > len(smaller) + 1:
        return kthSmallest(larger, k-len(smaller)-1)
    else:
        return kthSmallest(smaller, len(smaller) - 1)


A = [int(x) for x in input().split(',')]
k = int(input())

print(kthSmallest(A, k))
