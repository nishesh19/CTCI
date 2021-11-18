'''
Given InOrder and Pre-Order traversal,contruct the binary tree
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


def inOrder(root: Node):
    # Write your code here
    if(root):
        inOrder(root.left)
        print(root.info, end=" ")
        inOrder(root.right)


def constructTree(inOrder, preOrder):

    if len(preOrder) > 0:
        value = preOrder[0]
        root = Node(value)

        partition = inOrder.index(value)
        root.left = constructTree(
            inOrder[:partition], preOrder[1:partition + 1])
        root.right = constructTree(
            inOrder[partition + 1:], preOrder[partition + 1:])
        return root
    return None


def evaluate(root: Node):
    if root:
        op1 = evaluate(root.left)
        op2 = evaluate(root.right)
        operator = root.info

        if op1 and op2:
            root.info = operation(op1, op2, operator)

        return root.info

    return None


def operation(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a*b
    else:
        return a/b


if __name__ == '__main__':
    tree = BinarySearchTree()

    inOrder = [3, '*', 4, '/', 5, '+', 2, '+', 3, '*', 4]
    preOrder = ['+', '/', '*', 3, 4, 5, '+', 2, '*', 3, 4]

    root = constructTree(inOrder, preOrder)

    print(evaluate(root))
