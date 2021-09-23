from LinkedList import LinkedList, Node


def partition(head, partition_num):
    left = []
    right = []
    while head is not None:
        left.append(head.data) if head.data < partition_num else right.append(head.data)
        head = head.next
    ll = LinkedList()
    for i in left:
        node = Node(i)
        ll.addToTail(node)
    for i in right:
        node = Node(i)
        ll.addToTail(node)
    return ll


if __name__ == '__main__':
    linkedList = LinkedList()

    one = Node(1)
    two = Node(3)
    three = Node(4)
    four = Node(1)
    five = Node(1)
    six = Node(5)
    seven = Node(6)
    eight = Node(2)
    nine = Node(5)

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

    partition(linkedList.head, 4).printList()
    print("\n")
