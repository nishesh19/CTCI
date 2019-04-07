'''
2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
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

class LinkedList:
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

    def remove_duplicates(self):
        outer = self.head
        prev = self.head
        
        while outer:
            inner = outer.next
            
            while inner:
                if outer.value == inner.value:
                    prev.next = inner.next
                else:
                    prev = inner
                inner = inner.next
        
            outer = outer.next

if __name__ == '__main__':
    no_of_nodes = int(input())

    linkedList = LinkedList()
    for i in range(no_of_nodes):
        linkedList.insert(int(input()))

    linkedList.remove_duplicates()
    linkedList.iterate()

    