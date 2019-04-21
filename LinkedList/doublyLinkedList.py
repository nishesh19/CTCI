class Node:
    
    def __init__(self, value):
        self._next = None
        self._prev = None
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

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self,prev):
        self._prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, item):
        newNode = Node(item)
        
        if self.head == None:
            self.head = newNode
        
        if self.tail:
            self.tail.next = newNode
            newNode.prev = self.tail
        
        self.tail = newNode
        self.tail.next = self.head

    def iterate(self):
        head = self.head
        
        while True:
            print(head.value)
            
            if head == self.tail:
                break
            
            head = head.next
            

if __name__ == '__main__':
    no_of_nodes = int(input())

    dl = DoublyLinkedList()
    for i in range(no_of_nodes):
        dl.insert(int(input()))

    dl.iterate()

    