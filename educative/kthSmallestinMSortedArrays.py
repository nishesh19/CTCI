from heapq import heappush, heappop


class HeapNumber:
  def __init__(self, value, row, column):
    self.value = value
    self.row = row
    self.column = column

  def __lt__(self, other):
    return self.value < other.value


def find_Kth_smallest(lists, k):
  min_heap = []
  for i in range(len(lists)):
    heappush(min_heap, HeapNumber(lists[i][0], i, 0))

  while min_heap:
    heap_num = heappop(min_heap)
    num, row, column = heap_num.value, heap_num.row, heap_num.column
    print(str(num), end=" ")
    if k-1 == 0:
      return num

    k -= 1

    if column + 1 < len(lists[row]):
      heappush(min_heap, HeapNumber(lists[row][column+1], row, column+1))

  return -1


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()
