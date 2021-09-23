from LinkedList import LinkedList, Node


def deleteMiddleNode(node):
    if node is None:
        return
    if node.next is None: # last node
        node = None
        return
    node.data = node.next.data
    node.next = node.next.next


if __name__ == '__main__':
    linkedList = LinkedList()

    one = Node(1)
    two = Node(3)
    three = Node(4)
    four = Node(1)
    five = Node(1)
    six = Node(5)
    seven = Node(4)

    linkedList.addToHead(seven)
    linkedList.addToHead(six)
    linkedList.addToHead(five)
    linkedList.addToHead(four)
    linkedList.addToHead(three)
    linkedList.addToHead(two)
    linkedList.addToHead(one)

    linkedList.printList()
    print("\n")

    deleteMiddleNode(linkedList.head.next.next)

    linkedList.printList()
    print("\n")
