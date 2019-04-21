'''
2.S Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-) 1 -) 6) + (5 -) 9 -) 2) .Thatis,617 + 295.
Output: 2 -) 1 -) 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
Input: (6 -) 1 -) 7) + (2 -) 9 -) 5).Thatis,617 + 295.
Output: 9 -) 1 -) 2. That is, 912.
Hints: #7, #30, #71, #95, #109
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

    def iterate(self):
        head = self.head
        print('\n')
        while head:
            print(head.value,end=' ')
            head = head.next


def total(num1, num2,result):
    carry = 0
    head1 = num1.head
    head2 = num2.head
    while (head1) or (head2):
        value1 = head1.value if head1 else 0
        value2 = head2.value if head2 else 0

        total = value1 + value2 + carry
        carry = total // 10

        head1 = head1.next if head1 else None
        head2 = head2.next if head2 else None

        result.insert((total % 10) if head1 or head2 else total)

if __name__ == '__main__':
    num1 = SinglyLinkedList()

    for i in input().split(' '):
        num1.insert(int(i))

    num2 = SinglyLinkedList()

    for i in input().split(' '):
        num2.insert(int(i))
    
    result = SinglyLinkedList()
    total(num1,num2,result)
    result.iterate()



