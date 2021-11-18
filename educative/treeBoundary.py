from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_tree_boundary(root):
    if not root:
        return []

    result = deque()
    queue = deque([(0, root)])
    curr_level = 0
    prev_node = None

    while queue:
        level, node = queue.popleft()

        if level != curr_level:
            if prev_node.left or prev_node.right:
                result.append(prev_node)
            if node.left or node.right:
                result.append(node)

            curr_level = level

        if (not node.left) and (not node.right):
            result.append(node)

        if node.left:
            queue.append((level+1, node.left))

        if node.right:
            queue.append((level+1, node.right))

        prev_node = node

    return list(result)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(9)
    root.left.right = TreeNode(3)
    root.left.right.left = TreeNode(15)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(6)
    result = find_tree_boundary(root)
    print("Tree boundary: ", end='')
    for node in result:
        print(str(node.val) + " ", end='')
    print()

main()
