import os


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def topView(root):
    # Write your code here
    q = []
    vOrders = {}
    if root:
        q.append((root, 0))

    while q:
        curr_item = q.pop(0)
        curr_node = curr_item[0]
        curr_order = curr_item[1]
        if curr_node:
            if curr_order not in vOrders:
                vOrders[curr_order] = curr_node.info
            q.append((curr_node.left, curr_order - 1))
            q.append((curr_node.right, curr_order + 1))

    printTopView(vOrders)


def printTopView(verticalOrders: dict):
    for key in sorted(verticalOrders.keys()):
        print(verticalOrders[key], end=' ')


tree = BinarySearchTree()
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'topViewInput.txt')
with open(my_file) as f:
    for value in f.readline().split(' '):
        tree.create(int(value))

# t = int(input())

# arr = list(map(int, input().split()))

# for i in range(t):
#     tree.create(arr[i])

topView(tree.root)
print()
