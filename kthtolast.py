'''
2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
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

    def size(self):
        head = self.head
        length = 0

        while head:
            length += 1
            head = head.next
        
        return length
        
    def iterate(self):
        head = self.head
        print('\n\n')
        while head:
            print(head.value)
            head = head.next

    def kth_to_last(self,k):
        front = self.head
        
        while k > 0:
            front = front.next
            k -= 1
        
        back = self.head
        while front:
            front = front.next
            back = back.next

        return back.value
        

if __name__ == '__main__':
    nodes = input().split()

    no_of_nodes = int(nodes[0])
    k = int(nodes[1])

    sl = SinglyLinkedList()
    for i in range(no_of_nodes):
        sl.insert(int(input()))

    print(sl.kth_to_last(k))
    
    

    