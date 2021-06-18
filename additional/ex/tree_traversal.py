# Our Tree structure
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = Node(root)

tree = Tree(3)
tree.root.left = Node(9)
tree.root.right = Node(20)
tree.root.right.left = Node(15)
tree.root.right.right = Node(7)


def inorder(root, visited):
    if root:
        visited = inorder(root.left, visited)
        visited.append(root.data)
        visited = inorder(root.right, visited)
    return visited

def preorder(root, visited):
    if root:
        visited.append(root.data)
        visited = preorder(root.left, visited)
        visited = preorder(root.right, visited)
    return visited  # return visited stack

def postorder(root, visited):
    if root:  # check if node exits
        visited = postorder(root.left, visited)
        visited = postorder(root.right, visited)
        visited.append(root.data)
    return visited

print(f'Inorder (L-V-R)', inorder(tree.root, []))
print(f'Preorder (V-L-R)', preorder(tree.root, []))
print(f'Postorder (L-R-v)', postorder(tree.root, []))