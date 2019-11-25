import collections

Rectangle = collections.namedtuple('Rectangle',('x','y'))

R1 = Rectangle(x=1,y=2)
print(R1.x)
print(R1.y)