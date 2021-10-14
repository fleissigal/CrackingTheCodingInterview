from collections import deque

import Graph
from BTNode import BTNode, printTree
from LinkedList import LinkedList, Node


def nodeListByDepth(root):
    result = []
    if root is None:
        return result
    currList = [root]

    while len(currList) > 0:
        nextList = []
        ll = LinkedList()
        for currNode in currList:
            if currNode.left:
                nextList.append(currNode.left)
            if currNode.right:
                nextList.append(currNode.right)
            ll.addToTail(Node(currNode.data))
        result.append(ll)
        currList = nextList
    return result


if __name__ == '__main__':
    root = BTNode(1)

    root.left = BTNode(3)
    root.right = BTNode(2)

    root.left.left = BTNode(4)
    root.left.right = BTNode(5)
    root.right.left = BTNode(7)
    root.right.right = BTNode(6)

    root.right.right.left = BTNode(8)

    print(printTree(root))
    print("\n")

    result = nodeListByDepth(root)
    for nodesList in result:
        nodesList.printList()
        print("\n")


