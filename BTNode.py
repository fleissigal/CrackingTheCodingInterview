# A class to represent a Node object (a node in a binary tree)
class BTNode:
    # Constructor
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to print tree nodes inorder
def printTree(root):
    if root.left is not None:
        printTree(root.left)
    print(root.data)
    if root.right is not None:
        printTree(root.right)
