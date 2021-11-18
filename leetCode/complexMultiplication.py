class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        num11, num12 = 0, 0
        num21, num22 = 0, 0
        real, cmplx = 0, 0
        multliplier1 = -1 if a[0] == '-' else 1

        index1 = a.index('+')
        num11 = multliplier1*int(a[1 if a[0] == '-' else 0:index1])

        if a[index1+1] == '-':
            multliplier1 = -1
            index1 += 2
        else:
            multliplier1 = 1
            index1 += 1

        num12 = multliplier1*(int(a[index1:a.index('i')]))

        multliplier2 = -1 if b[0] == '-' else 1
        index2 = b.index('+')

        num21 = multliplier2 * int(b[1 if b[0] == '-' else 0:index2])

        if b[index2 + 1] == '-':
            multliplier2 = -1
            index2 += 2
        else:
            multliplier2 = 1
            index2 += 1

        num22 = multliplier2*int(b[index2:b.index('i')])

        real = num11 * num21 - num12*num22
        cmplx = num11*num22 + num21*num12
        
        real = ('-' + str(abs(real)) if real < 0 else str(real))
        cmplx = ('-' + str(abs(cmplx)) if cmplx < 0 else str(cmplx)) + 'i'
        
        return real + '+' + cmplx


if __name__ == '__main__':
    a = '-0+-0i'
    b = '-0+-0i'

    sol = Solution()
    print(sol.complexNumberMultiply(a, b))
