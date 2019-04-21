'''
https://www.hackerrank.com/challenges/maximum-element/problem
'''


import os


class MyQueue(object):
    def __init__(self):
        self.__queue = []
        self.__max = []
    
    def max(self):
        return self._MyQueue__max[-1]
        
    def pop(self):
        item =  self.__queue.pop()
        if item == self._MyQueue__max[-1]:
            self._MyQueue__max.pop()
        return item
        
    def push(self, value):
        self.__queue.append(value)        
        if (not self._MyQueue__max) or (value >= self._MyQueue__max[-1]):
            self._MyQueue__max.append(value)

queue = MyQueue()

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'maxElementInput.txt')
my_write_file = os.path.join(THIS_FOLDER, 'maxElementOutput.txt')
    
lines = []
    
with open(my_file) as f:
    with open(my_write_file,'w') as write_file:
        for line in f:
            values = map(int, line.rstrip().split())
            values = list(values)
            if values[0] == 1:
                queue.push(values[1])        
            elif values[0] == 2:
                queue.pop()
            else:
                print(queue.max())
                write_file.write(str(queue.max())+'\n')
                

