def mergeSort(A):
    if len(A) > 1:
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]

        mergeSort(left)
        mergeSort(right)

        merge(left, right, A)


def merge(left, right, A):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    A = [int(x) for x in input().split(',')]
    # 170,45,75,90,802,24,2,66
    print(f'Before Sort : {A}')
    # auxiliary = [None for i in range(len(A))]
    mergeSort(A)
    print(f'After Sort : {A}')
