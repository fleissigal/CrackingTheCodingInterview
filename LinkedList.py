class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToHead(self, node):
        node.next = self.head
        self.head = node
        if node.next is None:
            self.tail = node

    def addToTail(self, node):
        if self.tail is None: # This is the first element we are adding
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def printList(self):
        node = self.head
        while node is not None:
            print(str(node.data) + " -> ")
            node = node.next
