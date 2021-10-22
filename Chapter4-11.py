from BTNode import BTNode, printTree
# Solution to question 4.11

"""
Can be found in the file BTNode.py under the function randomNode()

Explanation on how to handle the other BST functions:

Insert - simply update each node we are passing with +1 to the leftNumNodes or rightNumNodes,
according to where the new node "went" during the insert process

Find - don't need to update anything

Delete - simply update each node we are passing with -1 to the leftNumNodes or rightNumNodes,
according to where the node we want to delete is found during the deletion process

"""

if __name__ == '__main__':

    root = BTNode(8)
    root.setLeftNumNodes(3)
    root.setRightNumNodes(2)

    root.left = BTNode(4)
    root.left.setLeftNumNodes(1)
    root.left.setRightNumNodes(1)

    root.right = BTNode(10)
    root.right.setLeftNumNodes(0)
    root.right.setRightNumNodes(1)

    root.left.left = BTNode(2)
    root.left.left.setLeftNumNodes(0)
    root.left.left.setRightNumNodes(0)

    root.left.right = BTNode(6)
    root.left.right.setLeftNumNodes(0)
    root.left.right.setRightNumNodes(0)

    root.right.right = BTNode(20)
    root.right.right.setLeftNumNodes(0)
    root.right.right.setRightNumNodes(0)

    print(printTree(root))
    print("\n")

    print(root.randomNode())

