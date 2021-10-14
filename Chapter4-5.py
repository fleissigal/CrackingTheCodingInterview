import math
from collections import deque

import Graph
from BTNode import BTNode, printTree
from LinkedList import LinkedList, Node


def validBSTAux(node, low, high):
    if node is None:
        return True
    if low >= node.data or node.data > high:
        return False
    return validBSTAux(node.left, low, node.data) and validBSTAux(node.right, node.data, high)


def validBST(root):
    return validBSTAux(root, -math.inf, math.inf)


if __name__ == '__main__':
    root = BTNode(8)

    root.left = BTNode(4)
    root.right = BTNode(10)

    root.left.left = BTNode(2)
    root.left.right = BTNode(6)
    root.right.right = BTNode(20)

    print(printTree(root))
    print("\n")

    print(validBST(root))

    print("\n")

    secondRoot = BTNode(8)

    secondRoot.left = BTNode(4)
    secondRoot.right = BTNode(10)

    secondRoot.left.left = BTNode(2)
    secondRoot.left.right = BTNode(12)
    secondRoot.right.right = BTNode(20)

    print(printTree(secondRoot))
    print("\n")

    print(validBST(secondRoot))
