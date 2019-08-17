'''
4.3 List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth 0, you'll have 0 linked lists).
'''


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


def depthList(root: Node):
    # Write your code here

    q = []
    vOrders = {}
    if root:
        q.append((root, 0))

    while q:
        curr_item = q.pop(0)
        curr_node = curr_item[0]
        curr_depth = curr_item[1]
        if curr_node:
            if curr_depth in vOrders:
                vOrders[curr_depth].append(curr_node.info)
            else:
                vOrders[curr_depth] = [curr_node.info]
            q.append((curr_node.left, curr_depth + 1))
            q.append((curr_node.right, curr_depth + 1))

    for order in sorted(vOrders.keys()):
        print(' '.join(map(str, vOrders[order])))


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

depthList(tree.root)
