'''
https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
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

class MyQueue(object):
    def __init__(self):
        self._oldest = MyStack()
        self._newest = MyStack()
    
    def peek(self):
        if self._oldest.isEmpty():
            while (not self._newest.isEmpty()):
                self._oldest.push(self._newest.pop())
        
        return self._oldest.peek()
        
    def dequeue(self):
        if self._oldest.isEmpty():
            while (not self._newest.isEmpty()):
                self._oldest.push(self._newest.pop())
            
        return self._oldest.pop()
        
    def enqueue(self, value):
        self._newest.push(value)
        
        

# queue = MyQueue()

# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join(THIS_FOLDER, 'maxElementInput.txt')
# my_write_file = os.path.join(THIS_FOLDER, 'maxElementOutput.txt')
    
# lines = []
    
# with open(my_file) as f:
#     with open(my_write_file,'w') as write_file:
#         for line in f:
#             values = map(int, line.rstrip().split())
#             values = list(values)
#             if values[0] == 1:
#                 queue.enqueue(values[1])        
#             elif values[0] == 2:
#                 print(queue.dequeue())
#             else:
#                 print(queue.peek())
#                 # write_file.write(str(queue.max())+'\n')
                

queue = MyQueue()


t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.enqueue(values[1])        
    elif values[0] == 2:
        queue.dequeue()
    else:
        print(queue.peek())

