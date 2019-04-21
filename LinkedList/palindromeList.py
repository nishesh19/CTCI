'''
2.6 Palindrome: Implement a function to check if a linked list is a palindrome
'''

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


def reverse(head):
    current = head
    prev = None

    while current:
        next = current.next
        current.next = prev

        prev = current
        current = next

    return prev

def isPalindrome(ll:SinglyLinkedList):
    middle = math.ceil(ll.size/2)

    current = ll.head

    while middle:
        current = current.next
        middle -= 1

    mid_reverse = reverse(current)

    current = ll.head

    while mid_reverse:
        if current.value != mid_reverse.value:
            return False
        
        current = current.next
        mid_reverse = mid_reverse.next

    
    return True

if __name__ == '__main__':

    sl = SinglyLinkedList()

    for i in input().split(' '):
        sl.insert(i)

    print(isPalindrome(sl))
