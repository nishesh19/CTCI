'''
Find the vertex cover for the given binary tree
    
'''

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None
        self.vertex_cover = 0

    def __str__(self):
        return str(self.info)

def constructTree(inOrder, preOrder):

    if len(preOrder) > 0:
        value = preOrder[0]
        root = Node(value)

        partition = inOrder.index(value)
        root.left = constructTree(inOrder[:partition], preOrder[1:partition + 1])
        root.right = constructTree(inOrder[partition + 1:], preOrder[partition + 1:])
        return root
    return None


def vertexCover(root: Node):
    if root:
        if root.vertex_cover !=0:
            return root.vertex_cover
            
        size_incl = 1 + vertexCover(root.left) + vertexCover(root.right)
        
        size_excl = 0

        if root.left:
            size_excl += 1 + vertexCover(root.left.left) + vertexCover(root.left.right)
            
        if root.right:
            size_excl += 1 + vertexCover(root.right.left) + vertexCover(root.right.right)
            
        
        root.vertex_cover = min(size_incl,size_excl)

        return root.vertex_cover
    
    return 0

if __name__ == '__main__':

    inOrder = [40,20,70,50,80,10,30,40]
    preOrder = [10,20,40,50,70,80,30,40]

    root = constructTree(inOrder, preOrder)
    
    print(vertexCover(root))
