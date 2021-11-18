from heapq import heappush, heappop, heappushpop


class MedianOfAStream:

    def __init__(self):
        self.first_half = []
        self.second_half = []

    def insert_num(self, num):
        if not self.second_half:
            heappush(self.second_half, num)
            return

        if num < self.second_half[0]:
            if len(self.first_half) < len(self.second_half):
                heappush(self.first_half, -num)
            else:
                heappush(self.second_half, -heappushpop(self.first_half, -num))
        else:
            if len(self.second_half) > len(self.first_half):
                heappush(self.first_half, -heappushpop(self.second_half, num))
            else:
                heappush(self.second_half, num)

    def find_median(self):
        # TODO: Write your code here
        if (not self.first_half) and (not self.second_half):
            return 0.0

        if len(self.first_half) == len(self.second_half):
            return (-self.first_half[0] + self.second_half[0])/2
        
        return self.second_half[0]
        


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
