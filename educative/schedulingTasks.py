from collections import defaultdict, deque
from heapq import heappush, heappop


def schedule_tasks(tasks, k):
    intervalCount = 0
    tasks_freq = defaultdict(int)

    for task in tasks:
        tasks_freq[task] += 1

    max_heap = []
    for key in tasks_freq:
        heappush(max_heap, (-tasks_freq[key], key))

    queue = deque()
    while True:
        if max_heap:
            freq, task = heappop(max_heap)
            queue.append((freq+1, task))
            print(task,end = " ")
        else:
            queue.append((0, None))
            print("Idle",end = " ")

        if len(queue) == k + 1:
            freq, task = queue.popleft()
            if task == None:
                break
            if freq != 0:
                heappush(max_heap, (freq, task))

        intervalCount += 1
        
    return intervalCount


def main():
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'b', 'a'], 3)))


main()
