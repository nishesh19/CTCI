from heapq import heapify, heappop, heappush
import math

class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        if self.start == other.start:
            return self.end < other.end

        return self.start < other.start


def min_meeting_rooms(meetings):
    # TODO: Write your code here
    if (not meetings):
        return 0
    meetings.sort(key=lambda x:(x.start,x.end))
    curr_meetings = [meetings[0]]
    min_rooms = 1

    for i in range(1,len(meetings)):
        while (curr_meetings) and meetings[i].start >= curr_meetings[0].end:
            heappop(curr_meetings)
        
        heappush(curr_meetings,meetings[i])
        min_rooms = max(min_rooms,len(curr_meetings))

    return min_rooms


def main():
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
        [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
    # print("Minimum meeting rooms required: " +
    #       str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    # print("Minimum meeting rooms required: " +
    #       str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    # print("Minimum meeting rooms required: " +
    #       str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    # print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    #     [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))


main()
