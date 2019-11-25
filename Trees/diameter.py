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


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def diameterOfBinaryTree(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    ldiameter = diameterOfBinaryTree(root.left)
    rdiameter = diameterOfBinaryTree(root.right)

    return max(lheight+rheight, max(ldiameter, rdiameter))


def height(root):
    if not root:
        return 0

    return 1 + max(height(root.left), height(root.right))


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

if __name__ == '__main__':

    inOrder = [4, 2, 5, 1, 3]
    preOrder = [1, 2, 4, 5, 3]

    root = constructTree(inOrder, preOrder)

    print(diameterOfBinaryTree(root))
