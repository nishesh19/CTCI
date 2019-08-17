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


def verticalOrder(root: Node):
    vOrder = {}
    populateOrder(root, vOrder, 0)
    printVerticalOrder(vOrder)


def printVerticalOrder(verticalOrders: dict):
    for key in sorted(verticalOrders.keys()):
        for item in verticalOrders[key]:
            print(item, end=' ')
        print()


def populateOrder(root: Node, vOrders: dict, currentOrder):
    if root:
        if currentOrder in vOrders:
            vOrders[currentOrder].append(root.info)
        else:
            vOrders[currentOrder] = [root.info]
        populateOrder(root.left, vOrders, currentOrder - 1)
        populateOrder(root.right, vOrders, currentOrder + 1)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

verticalOrder(tree.root)
