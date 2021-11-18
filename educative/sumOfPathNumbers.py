class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    # TODO: Write your code here
    if not root:
        return 0

    allPaths = []
    find_all_paths(root,[],allPaths)
    return sum(allPaths)


def find_all_paths(root, currentPath, allPaths):
    currentPath.append(root.val)

    if (not root.left) and (not root.right):
        allPaths.append(int(''.join([str(x) for x in currentPath])))

    if root.left:
        find_all_paths(root.left, currentPath, allPaths)

    if root.right:
        find_all_paths(root.right, currentPath, allPaths)

    currentPath.pop()


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
