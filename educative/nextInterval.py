from heapq import heappush, heappop


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals: Interval):
    if not intervals:
        return []

    min_end = []

    for i in range(len(intervals)):
        interval = intervals[i]
        heappush(min_end, (interval.start, i))

    # intervals.sort(key=lambda x: x.end)
    result = []
    for interval in intervals:
        while min_end and min_end[0][0] < interval.end:
            heappop(min_end)
        
        if not min_end:
            result.append(-1)
        else:
            result.append(min_end[0][1])
            
    # TODO: Write your code here
    return result


def main():

    result = find_next_interval(
        [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    # result = find_next_interval(
    #     [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    # print("Next interval indices are: " + str(result))


main()
