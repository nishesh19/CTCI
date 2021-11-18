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


def reorder(head: Node):
    # TODO: Write your code here
    fast = slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    rev = reverse(slow)

    curr = head
    next1, next2 = None, None

    while curr and rev and (rev != curr):
        next1 = curr.next
        next2 = rev.next

        curr.next = rev
        rev.next = next1 if rev != next1 else None

        curr = next1
        rev = next2

    return


def reverse(head):
    prev = next = None

    while head:
        next = head.next
        head.next = prev

        prev = head
        head = next

    return prev


def reverse_sub_list(head, p, q):
    # TODO: Write your code here
    if (not head) or (not head.next):
        return head

    j = 1
    bf_rev, af_rev = head, head
    while (j < q+1) and af_rev:
        if j < p-1:
            bf_rev = bf_rev.next

        af_rev = af_rev.next
        j += 1

    prev, rev, next = af_rev, bf_rev.next, None
    diff = q-p+1
    while rev and diff:
        next = rev.next
        rev.next = prev

        prev = rev
        rev = next

        diff -= 1

    bf_rev.next = prev

    return head


def reverse_every_k_elements(head, k):
    # TODO: Write your code here
    if (not head) or (not head.next) or (k == 1):
        return head

    curr = head
    new_head, prev_head = None, None
    while curr:
        prev, next = reverseK(curr, k)

        if not new_head:
            new_head = prev

        if prev_head:
            prev_head.next = prev

        prev_head = curr
        curr = next
    return new_head


def reverse_alternate_k_elements(head, k):
    if (not head) or (not head.next) or (k == 1):
        return head

    curr = head
    new_head, last_tail = None, None
    while curr:
        # 2,3
        prev, next = reverseK(curr, k)

        if not new_head:
            new_head = prev

        if last_tail:
          last_tail.next = prev
          
        curr.next = next
        jump = k

        while curr and jump:
            curr = curr.next
            jump -= 1

        last_tail = curr
        curr = curr.next if curr else None

    return new_head


def reverseK(head, k):
    prev, curr, next = None, head, None

    while curr and k:
        next = curr.next
        curr.next = prev

        prev = curr
        curr = next

        k -= 1

    return prev, curr

def rotate(head, rotations):
  # TODO: Write your code here
  if (not head) or (not head.next) or rotations == 0:
    return head

  curr = head
  list_len = 0

  while curr:
    list_len += 1
    curr = curr.next

  curr = head
  jump = (rotations%list_len) - 1

  while jump:
    curr = curr.next
    jump -= 1

  second_half_start = curr.next
  second_half_start_copy = second_half_start
  curr.next = None

  while second_half_start_copy.next:
    second_half_start_copy = second_half_start_copy.next
  
  second_half_start_copy.next = head

  return second_half_start


if __name__ == '__main__':

    sl = SinglyLinkedList()

    for i in range(1, 6):
        sl.insert(i)

    sl.head = rotate(sl.head,8)
    sl.iterate()
