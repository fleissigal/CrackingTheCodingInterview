from collections import deque

class MyQueue:
    def __init__(self):
        self.inStack = deque()
        self.outStack = deque()

    def push(self, item):
        self.moveAllItems("in")
        self.inStack.append(item)

    def pop(self):
        self.moveAllItems("out")
        return self.outStack.pop()

    def peek(self):
        self.moveAllItems("out")
        return self.outStack[0]

    def isEmpty(self):
        return len(self.inStack) == 0 and len(self.outStack) == 0

    def moveAllItems(self, stackName):
        if stackName == "in":
            if len(self.outStack) == 0:
                return
            else:
                while len(self.outStack) > 0:
                    self.inStack.append(self.outStack.pop())
        else:
            if len(self.inStack) == 0:
                return
            else:
                while len(self.inStack) > 0:
                    self.outStack.append(self.inStack.pop())


if __name__ == '__main__':

    myQueue = MyQueue()

    myQueue.push(1)
    myQueue.push(3)
    myQueue.push(5)
    myQueue.push(11)

    print(myQueue.pop())
    print("\n")

    myQueue.push(15)
    myQueue.push(17)
    myQueue.push(19)

    print(myQueue.pop())
    print(myQueue.pop())
    print(myQueue.pop())
    print(myQueue.pop())
    print(myQueue.pop())