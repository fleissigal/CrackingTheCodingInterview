from LinkedList import LinkedList, Node


def removeDups(head):
    ht = {}
    if head is None or head.next is None:
        return
    node = head
    ht[node.data] = 1
    while node.next is not None:
        if node.next.data in ht:
            node.next = node.next.next
        else:
            ht[node.data] = 1
            node = node.next


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

    removeDups(linkedList.head)

    linkedList.printList()
    print("\n")
