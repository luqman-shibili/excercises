class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Example tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=' ')
        inorder(node.right)

def preorder(node):
    if node:
        print(node.value, end=' ')
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=' ')

print("Inorder:"); inorder(root)
print("\nPreorder:"); preorder(root)
print("\nPostorder:"); postorder(root)