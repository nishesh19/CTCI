def countingSort(A):
    size = max(A) + 1
    auxiliary = [0 for i in range(size)]
    ordered = [None for i in range(len(A))]

    for i in range(len(A)):
        auxiliary[A[i]] += 1

    for i in range(2, size):
        auxiliary[i] += auxiliary[i-1]

    for i in range(len(A)):
        ordered[auxiliary[A[i]]-1] = A[i]
        auxiliary[A[i]] -= 1

    return ordered

if __name__ == '__main__':
    A = [int(x) for x in input().split(',')]
    print(countingSort(A))
