'''
3.S Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
Hints: # 75, #32, #43
'''
 
import os

class MyStack():
    def __init__(self):
        self._stack = []

    def push(self,value):
        self._stack.append(value)

    def pop(self):
        return self._stack.pop()

    def peek(self):
        return self._stack[-1]

    def isEmpty(self):
        return self._stack == []        

sorted_stack = MyStack()
temp_stack = MyStack()

def insert(value):
    if sorted_stack.isEmpty():
        sorted_stack.push(value)
    else:
        while (not sorted_stack.isEmpty()) and sorted_stack.peek() < value:
            temp_stack.push(sorted_stack.pop())
        
        sorted_stack.push(value)

        while (not temp_stack.isEmpty()):
            sorted_stack.push(temp_stack.pop())
            

def delete():
    return sorted_stack.pop()

def peek():
    return sorted_stack.peek()

t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        insert(values[1])
    elif values[0] == 2:
        print(delete())
    else:
        print(peek())

