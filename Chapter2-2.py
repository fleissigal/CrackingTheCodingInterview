from LinkedList import LinkedList, Node


def kthToLast(head, k):
    if head is None:
        return None
    length = 1
    node = head
    while node.next is not None:
        length += 1
        node = node.next
    if length - k - 1 < 0:
        return None
    else:
        node = head
        for i in range(length - k - 1):
            node = node.next
        return node.data


if __name__ == '__main__':
    linkedList = LinkedList()

    one = Node(1)
    two = Node(3)
    three = Node(4)
    four = Node(1)
    five = Node(1)
    six = Node(5)
    seven = Node(4)
    eight = Node(4)
    nine = Node(4)

    linkedList.addToHead(nine)
    linkedList.addToHead(eight)
    linkedList.addToHead(seven)
    linkedList.addToHead(six)
    linkedList.addToHead(five)
    linkedList.addToHead(four)
    linkedList.addToHead(three)
    linkedList.addToHead(two)
    linkedList.addToHead(one)

    linkedList.printList()
    print("\n")

    print(kthToLast(linkedList.head, 1))
    print(kthToLast(linkedList.head, 3))
    print(kthToLast(linkedList.head, 5))
    print(kthToLast(linkedList.head, 20))

    print("\n")

    linkedListTwo = LinkedList()
    print(kthToLast(linkedListTwo.head, 1))
    print(kthToLast(linkedListTwo.head, 2))

    one = Node(1)
    linkedListTwo.addToHead(one)
    print(kthToLast(linkedListTwo.head, 0))
    print(kthToLast(linkedListTwo.head, 1))

