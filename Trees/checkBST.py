import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

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
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
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


def check_binary_search_tree(root: Node, min, max):
    if root:
        if not (min < root.data < max):
            return False
        lt = True
        rt = True
        if root.left:
            lt = (root.data > root.left.data) and check_binary_search_tree(root.left, min, root.data)
        if root.right:
            rt = (root.data < root.right.data) and check_binary_search_tree(root.right, root.data, max)
            
        return lt & rt
    return True

def check_binary_search_tree_(root):
    return check_binary_search_tree(root, -1-sys.maxsize, sys.maxsize)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

ans = check_binary_search_tree_(tree.root)
print(ans)
