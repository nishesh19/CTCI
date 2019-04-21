'''
3.6 Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linked List data structure.
Hints: #22, #56, #63
'''
 
import os

class Queue():
    def __init__(self):
        self._queue = []

    def enqueue(self,value):
        self._queue.append(value)

    def dequeue(self):
        return self._queue.pop(0)

    def peek(self):
        return self._queue[0]

    def isEmpty(self):
        return self._queue == []

class Animal():
    def __init__(self):
        self._order = None

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self,value):
        self._order = value


class Dog(Animal):
    def __init__(self):
        pass

class Cat(Animal):
    def __init__(self):
        pass
        
class AnimalShelter():
    def __init__(self):
        self._dogs = []
        self._cats = [] 
        self._order = 1

    def enqueue(self, animal:Animal):
        animal.order = self._order
        
        if isinstance(animal,Dog):
            self._dogs.append(animal)
        else:
            self._cats.append(animal)
        
        self._order += 1    
    
    def dequeueDog(self):
        return self._dogs.pop(0)

    def dequeueCat(self):
        return self._cats.pop(0)
    
    def dequeueAny(self):
        if self._dogs[0].order < self._cats[0].order:
            return self.dequeueDog()
        else:
            return self.dequeueCat()

shelter = AnimalShelter()

d1 = Dog()
d2 = Dog()
d3 = Dog()

c1 = Cat()
c2 = Cat()
c3 = Cat()

shelter.enqueue(d1)
shelter.enqueue(c1)

print(shelter.dequeueCat())

shelter.enqueue(d2)
shelter.enqueue(c2)

print(shelter.dequeueAny())

shelter.enqueue(c3)
shelter.enqueue(d3)

print(shelter.dequeueDog())
