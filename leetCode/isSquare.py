import math


class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        d12 = self.distance(p1, p2)
        d13 = self.distance(p1, p3)
        d14 = self.distance(p1, p4)
        d23 = self.distance(p2, p3)
        d24 = self.distance(p2, p4)
        d34 = self.distance(p3, p4)

        if (d12 == d14) and (math.isclose(math.pow(d13, 2), 2*math.pow(d12, 2))) and (d23 == d34 == d12):
            return True
        elif (d12 == d13) and (math.isclose(math.pow(d14, 2), 2*math.pow(d12, 2))) and (d24 == d34 == d12):
            return True
        elif (d13 == d14) and (math.isclose(math.pow(d12, 2), 2*math.pow(d14, 2))) and (d23 == d24 == d14):
            return True

        return False

    def distance(self, p1, p2):
        return math.sqrt(math.pow(p1[0]-p2[0], 2) + math.pow(p1[1]-p2[1], 2))


if __name__ == '__main__':
    sol = Solution()
    p3 = [10, 20]
    p1 = [20, 20]
    p4 = [20, 10]
    p2 = [10, 10]
    print(sol.validSquare(p1, p2, p3, p4))
