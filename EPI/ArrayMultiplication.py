

'''
Write a program that takes two arrays represting integers and returns an
integer represeting their product
'''
def mult(A: list, B: list, isNegative: bool):
    result = []
    position = 1

    for a in reversed(A):
        carry = 0
        i = position

        for b in reversed(B):
            res_len = len(result)
            temp_sum = a*b + carry
            carry = temp_sum // 10
            if i > res_len:
                result.insert(0, temp_sum % 10)
            else:
                temp_sum = (temp_sum % 10) + result[res_len - i]
                carry += temp_sum // 10
                result[res_len - i] = temp_sum % 10
            i += 1

        if carry:
            result.insert(0, carry)
            carry = 0
        position += 1

    if carry:
        result.insert(0, carry)

    if isNegative:
        result[0] = -result[0]
    return result


num1 = input()
num2 = input()
isNum1Neg = True if num1[0] == '-' else False
isNum2Neg = True if num2[0] == '-' else False
A = [int(x) for x in num1 if x != '-']
B = [int(x) for x in num2 if x != '-']

print(mult(A, B, (isNum1Neg ^ isNum2Neg)))
