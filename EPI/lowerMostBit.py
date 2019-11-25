def setLowerMostZero(n):
    index = 0
    m = n
    while m:
        if m & 1 == 0:
            break
        m >>= 1
        if(m):
            index += 1
    mask = 1 << index
    n |= mask
    return n


def clearLowerMostSetBit(n):
    return n & (n-1)


n = int(input())
print(f'Orginal Number = {bin(n)}')
print(f'After Lower most zero set = {bin(setLowerMostZero(n))}')
print(f'After Lower most set bit cleared = {bin(n&(n-1))}')
print(f'Lower Most Set bit is {n&-n}')
print(f'Number of ones = {bin(n).count("1")}')
print(f'Number of zeros = {bin(n).count("0")}')
