'''
2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting

https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def size(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    
    return length

def findMergeNode(head1, head2):
    size1 = size(head1)
    size2 = size(head2)

    current1 = head1
    current2 = head2

    if size1>size2:
        diff = size1-size2
        while diff:
            current1 = current1.next
            diff -= 1
    elif size2>size1:
        diff = size2 - size1
        while diff:
            current2 = current2.next
            diff -= 1
    
    while current1.next and current2.next:
        if (current1.next.data == current2.next.data) and (current1.next.next == current2.next.next):
            return current1.next.data
        
        current1 = current1.next
        current2 = current2.next

    return current1.data
if __name__ == '__main__':

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)
            
        ptr1 = llist1.head;
        ptr2 = llist2.head;

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next
                
        for i in range(llist2_count):
            if i != llist2_count-1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        print(str(result) + '\n')