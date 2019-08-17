
'''
Count the no of 1's in the given number
'''
def count_bits(n):
    no_of_bits = 0
    while n:
        no_of_bits += n & 1
        n >>= 1
    return no_of_bits


n = int(input())
print(f'Binary Representation = {bin(n)}')
print(f'No of ones: {count_bits(n)}')
