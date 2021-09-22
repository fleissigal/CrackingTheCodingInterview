class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addToHead(self, node):
        node.next = self.head
        self.head = node

    def printList(self):
        node = self.head
        while node is not None:
            print(str(node.data) + " -> ")
            node = node.next
