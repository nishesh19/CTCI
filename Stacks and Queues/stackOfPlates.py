'''
3.3 Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack
(that is, pop ( ) should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt (int index) which performs a pop operation on a specific sub-stack.
'''


import os


class SetOfStacks(object):
    def __init__(self, capacity):
        self.__stacks = []
        if capacity < 1:
            raise Exception('Stack Capacity should atleast be 1')
        self.__capacity = capacity

    def pop(self):
        try:
            if (not self._SetOfStacks__stacks[-1]):
                del self._SetOfStacks__stacks[-1]
            
            return self._SetOfStacks__stacks[-1].pop()
        except Exception as ex:
            print(ex)

    def push(self, value):
        if (not self._SetOfStacks__stacks) or (len(self._SetOfStacks__stacks[-1]) >= self._SetOfStacks__capacity):
            self._SetOfStacks__stacks.append([])

        self._SetOfStacks__stacks[-1].append(value)

    def popAt(self,index):
        try:
            return self._SetOfStacks__stacks[index].pop()
        except Exception as ex:
            print(ex)


if __name__ =='__main__':
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'maxElementInput.txt')

    setofStacks = SetOfStacks(1)
    i = -1
    with open(my_file) as f:
        for line in f:
            values = map(int, line.rstrip().split())
            values = list(values)
            if values[0] == 1:
                setofStacks.push(values[1])        
                i += 1
            elif values[0] == 2:
                print(setofStacks.pop())
                i -= 1
            else:
                print(setofStacks.popAt(i))

