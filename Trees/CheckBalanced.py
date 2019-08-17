'''
4.4 Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.
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


def isBalanced(root: Node, nodeHeights: dict):
    # Write your code here
    if not root:
        return True

    lh = height(root.left, nodeHeights)
    rh = height(root.right, nodeHeights)

    if (abs(lh - rh) <= 1) and isBalanced(root.left, nodeHeights) and isBalanced(root.right, nodeHeights):
        return True

    return False


def height(root: Node, nodeHeights: dict):
    if root in nodeHeights:
        return nodeHeights[root]

    if root:
        nodeHeights[root] = 1 + max(height(root.left,
                                           nodeHeights), height(root.right, nodeHeights))
        return nodeHeights[root]
    return 0


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

nodeHeights = {}
print(isBalanced(tree.root, nodeHeights))
