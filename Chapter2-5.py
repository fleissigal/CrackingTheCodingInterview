from LinkedList import LinkedList, Node


def sumLists(head1, head2):
    numToWrite = 0
    numToCarry = 0
    nextVal1 = 0
    nextVal2 = 0
    res = LinkedList()

    while True:
        if head1 is None and head2 is None:
            break

        if head1 is not None:
            nextVal1 = head1.data
            head1 = head1.next
        else:
            nextVal1 = 0
        if head2 is not None:
            nextVal2 = head2.data
            head2 = head2.next
        else:
            nextVal2 = 0

        sum = nextVal1 + nextVal2 + numToCarry
        numToWrite = sum % 10
        numToCarry = sum // 10
        res.addToTail(Node(numToWrite))

    if numToCarry > 0:
        res.addToTail(Node(numToCarry))
    return res



if __name__ == '__main__':
    linkedList1 = LinkedList()

    one = Node(9)
    two = Node(7)
    three = Node(8)

    linkedList1.addToTail(one)
    linkedList1.addToTail(two)
    linkedList1.addToTail(three)

    linkedList2 = LinkedList()

    four = Node(6)
    five = Node(8)
    six = Node(5)

    linkedList2.addToTail(four)
    linkedList2.addToTail(five)
    linkedList2.addToTail(six)

    linkedList1.printList()
    print("\n")
    linkedList2.printList()
    print("\n")
    print("\n")

    sumLists(linkedList1.head, linkedList2.head).printList()
    print("\n")




    linkedList3 = LinkedList()

    one = Node(9)
    two = Node(7)
    three = Node(8)
    four = Node(5)

    linkedList3.addToTail(one)
    linkedList3.addToTail(two)
    linkedList3.addToTail(three)
    linkedList3.addToTail(four)

    linkedList4 = LinkedList()

    five = Node(8)
    six = Node(5)
    seven = Node(6)

    linkedList4.addToTail(five)
    linkedList4.addToTail(six)
    linkedList4.addToTail(seven)

    linkedList3.printList()
    print("\n")
    linkedList4.printList()
    print("\n")
    print("\n")

    sumLists(linkedList3.head, linkedList4.head).printList()
    print("\n")