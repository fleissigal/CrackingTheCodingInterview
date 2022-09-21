from BTNode import BTNode, printTree


def successor(root, value):
    res = None
    node = root.find(value)
    if node is None:
        return "Value not found"

    if node.right:
        res = node.right
        while res.left is not None:
            res = res.left
        return res.data
    else:
        while node.parent:
            if node.parent.left:
                if node.parent.left.data == node.data:
                    return node.parent.data
            node = node.parent

    return None

if __name__ == '__main__':
    root = BTNode(8)

    root.left = BTNode(4)
    root.left.parent = root

    root.right = BTNode(11)
    root.right.parent = root

    root.left.left = BTNode(1)
    root.left.left.parent = root.left
    root.left.right = BTNode(6)
    root.left.right.parent = root.left
    root.right.left = BTNode(9)
    root.right.left.parent = root.right
    root.right.right = BTNode(14)
    root.right.right.parent = root.right

    root.right.left.right = BTNode(10)
    root.right.left.right.parent = root.right.left
    root.left.right.left = BTNode(5)
    root.left.right.left.parent = root.left.right
    root.left.right.right = BTNode(7)
    root.left.right.right.parent = root.left.right

    print(printTree(root))
    print("\n")

    result = successor(root, 8)
    print(result)

    result = successor(root, 7)
    print(result)

    result = successor(root, 10)
    print(result)

    result = successor(root, 14)
    print(result)