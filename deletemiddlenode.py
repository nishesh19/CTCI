'''
2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
Input: the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f
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
        print('\n')
        while head:
            print(head.value)
            head = head.next

    def delete(self,node):
        node.value = node.next.value
        node.next = node.next.next


if __name__ == '__main__':
    nodes = input().split()

    no_of_nodes = int(nodes[0])
    k = int(nodes[1])

    sl = SinglyLinkedList()
    for i in range(no_of_nodes):
        sl.insert(int(input()))

    head = sl.head
    while k>0:
        head = head.next
        k -= 1

    print(f'Node to delete : {head.value}')

    sl.delete(head)
    print('Updated list')
    sl.iterate()
    
    
    

    