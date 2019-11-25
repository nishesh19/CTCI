import math


def countingSort(A, power):
    size = 10
    auxiliary = [0 for i in range(size)]
    ordered = [None for i in range(len(A))]

    for i in range(len(A)):
        index = int((A[i] // power) % 10)
        auxiliary[index] += 1

    for i in range(1, size):
        auxiliary[i] += auxiliary[i-1]

    for i in reversed(range(len(A))):
        index = int((A[i] // power) % 10)
        ordered[auxiliary[index]-1] = A[i]
        auxiliary[index] -= 1

    for i in range(len(A)):
        A[i] = ordered[i]


def radixSort(A):
    digits = int(math.log(max(A), 10))
    for digit in range(digits+1):
        power = math.pow(10, digit)
        countingSort(A, power)


if __name__ == '__main__':
    A = [int(x) for x in input().split(',')]
    # 170,45,75,90,802,24,2,66
    print(f'Before Sort : {A}')
    radixSort(A)
    print(f'After Sort : {A}')
