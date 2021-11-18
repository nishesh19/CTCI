from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def rotate(head, rotations):
  # TODO: Write your code here
  if (not head) or (not head.next) or rotations == 0:
    return head

  curr = head
  ll_len = 1

  while curr.next:
    ll_len += 1
    curr = curr.next

  jumps = rotations % ll_len

  curr = head

  while jumps > 1:
    curr = curr.next
    jumps -= 1

  new_head = curr.next
  curr.next = None

  new_tail = new_head

  while new_tail.next:
    new_tail = new_tail.next
  
  new_tail.next = head
  head = new_head

  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = rotate(head, 3)
  print("Nodes of rotated LinkedList are: ", end='')
  result.print_list()


main()
