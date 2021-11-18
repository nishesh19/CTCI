from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root: TreeNode):
    if not root:
        return []

    result = deque()
    queue = deque([(0, root)])
    r_len = 0

    while queue:
        level, node = queue.popleft()

        if (r_len == 0) or (level == r_len):
            result.appendleft([node.val])
            r_len += 1
        else:
            result[0].append(node.val)

        if node.left:
            queue.append((level+1, node.left))

        if node.right:
            queue.append((level+1, node.right))

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()
