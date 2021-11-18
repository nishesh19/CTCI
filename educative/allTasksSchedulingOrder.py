from itertools import permutations
from collections import defaultdict, deque


def print_orders(tasks, prerequisites):
    all_orders = [[]]
    graph = defaultdict(list)
    indegrees = defaultdict(int)
    source = deque()

    for prereq in prerequisites:
        graph[prereq[0]].append(prereq[1])
        indegrees[prereq[1]] += 1

    for task in range(tasks):
        if indegrees[task] == 0:
            source.append(task)

    while source:
        n = len(all_orders)
        for _ in range(n):
            curr_order = all_orders.pop(0)
            for order in permutations(source):
                all_orders.append(curr_order + list(order))
        m = len(source)
        for _ in range(m):
            vertex = source.popleft()
            for child in graph[vertex]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    source.append(child)

    print(all_orders)


def main():
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
