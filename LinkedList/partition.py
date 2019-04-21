'''
2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5)
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
'''


class Node:

    def __init__(self, value):
        self._next = None
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, item):
        newNode = Node(item)
        if self.head == None:
            self.head = newNode

        if self.tail:
            self.tail.next = newNode

        self.tail = newNode

    def partition(self, partition_value):
        left,right = self.head,self.head

        while right:
            if right.value < partition_value:
                left.value,right.value = right.value,left.value
                left = left.next
            right = right.next

    def iterate(self):
        head = self.head
        print('\n\n')
        while head:
            print(head.value)
            head = head.next


if __name__ == '__main__':
    args = input().split(' ')
    no_of_nodes = int(args[0])

    sl = SinglyLinkedList()

    for i in range(no_of_nodes):
        sl.insert(int(input()))
    
    sl.partition(int(args[1]))
    sl.iterate()
