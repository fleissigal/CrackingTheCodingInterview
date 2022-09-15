from BTNode import BTNode, printTree


def minimalTree(arr):
    if len(arr) == 0:
        return None
    rootIdx = len(arr) // 2
    root = BTNode(arr[rootIdx])

    if len(arr) == 1:
        root.left = None
        root.right = None
    elif len(arr) == 2:
        root.left = BTNode(arr[0])
        root.right = None
    else:
        root.left = minimalTree(arr[0 : rootIdx])
        root.right = minimalTree(arr[rootIdx + 1 : ])

    return root


if __name__ == '__main__':
    arr = [1, 4, 7, 9, 10, 12, 14]
    treeRoot = minimalTree(arr)
    printTree(treeRoot)

    print("\n")

    arr = [1, 3, 4, 7, 8, 10, 12, 14]
    treeRoot = minimalTree(arr)
    printTree(treeRoot)

