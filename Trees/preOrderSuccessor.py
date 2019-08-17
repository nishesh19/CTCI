'''
4.6 Successor: Write an algorithm to find the "next" node (i .e., pre-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None
        self.parent = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        new_node = Node(val)
                        current.left = new_node
                        new_node.parent = current
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        new_node = Node(val)
                        current.right = new_node
                        new_node.parent = current
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,data): 
          self.data = data  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains data as data, left , right
'''


def getMax(root: Node):
    if root.right:
        return getMax(root.right)
    return root


def preOrderSuccessor(root: Node):
    if root.left:
        return root.left

    if root.right:
        return root.right

    while root.parent:
        if (root.parent.left == root) & (root.parent.right is not None):
            return root.parent.right
        root = root.parent

    return None


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(preOrderSuccessor(tree.root.right.left))
