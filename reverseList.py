

import math

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
        
    def iterate(self):
        head = self.head
        print('\n\n')
        while head:
            print(head.value)
            head = head.next

    @property
    def size(self):
        head = self.head
        length = 0

        while head:
            length += 1
            head = head.next

        return length

    def reverse(self):
        current = self.head
        prev = None

        while current:
            next = current.next
            current.next = prev

            prev = current
            current = next
        
        self.head = prev

if __name__ == '__main__':
    no_of_nodes = int(input())

    sl = SinglyLinkedList()
    
    for i in range(no_of_nodes):
        sl.insert(int(input()))

    sl.reverse()
    sl.iterate()

    