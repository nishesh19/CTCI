def quickSort(A, low, high):
    if low < high-1:
        index = partition(A, low, high)
        quickSort(A, low, index)
        quickSort(A, index + 1, high)
    pass


def partition(A, low, high):
    pivot = A[high-1]

    left, right = low, high-2
    while left < right:
        if A[left] <= pivot:
            left += 1
        else:
            A[left], A[right] = A[right], A[left]
            right -= 1

    left = left if A[left] > A[left + 1] else left + 1
    A[left], A[high-1] = A[high-1], A[left]
    return left


if __name__ == '__main__':
    A = [int(x) for x in input().split(',')]
    print(f'Before Sort : {A}')
    quickSort(A, 0, len(A))
    print(f'After Sort : {A}')
