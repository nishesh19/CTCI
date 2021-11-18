from heapq import heappush, heappop


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class IndexedInterval:
    def __init__(self, row, column, interval: Interval):
        self.row = row
        self.column = column
        self.interval = interval

    def __lt__(self, other):
        self.interval.start < other.interval.start


def find_employee_free_time(schedules):
    result = []
    intervals = []

    for i in range(len(schedules)):
        heappush(intervals, IndexedInterval(i, 0, schedules[i][0]))

    while intervals:
        curr_item = heappop(intervals)
        row, column, interval = curr_item.row, curr_item.column, curr_item.interval

        if column+1 < len(schedules[row]):
            heappush(intervals, IndexedInterval(
                row, column+1, schedules[row][column+1]))

        if not intervals:
            break
        
        next_interval = intervals[0].interval

        if interval.end < next_interval.start:
            result.append(Interval(interval.end, next_interval.start))

        # TODO: Write your code here
    return result


def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
