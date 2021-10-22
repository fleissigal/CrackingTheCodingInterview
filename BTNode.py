# A class to represent a Node object (a node in a binary tree)
import random


class BTNode:
    # Constructor
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        self.leftNumNodes = 0
        self.rightNumNodes = 0

    def setLeftNumNodes(self, num):
        self.leftNumNodes = num

    def setRightNumNodes(self, num):
        self.rightNumNodes = num

    # Solution to Chapter4-11
    def randomNode(self):
        if self is None:
            return -1
        # Base case
        if self.left is None and self.right is None:
            return self.data

        numNodes = self.leftNumNodes + self.rightNumNodes + 1

        rnd = random.randint(0, numNodes - 1)

        if rnd == 0:
            return self.data
        elif rnd <= self.leftNumNodes:
            return self.left.randomNode()
        else:
            return self.right.randomNode()


# Function to print tree nodes inorder
def printTree(root):
    if root.left is not None:
        printTree(root.left)
    print(root.data)
    if root.right is not None:
        printTree(root.right)
