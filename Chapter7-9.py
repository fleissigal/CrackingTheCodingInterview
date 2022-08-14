"""
Answer to Question 7.9

"""

class CircularArray:
    array = []
    head = 0 #holds the index of the head of the list at any given moment

    # moves the head to the right
    def rotateRight(self):
        return

    # moves the head to the left
    def rotateLeft(self):
        return

    def insert(self, value):
        return

    def remove(self, index):
        return

    def get(self, index):
        return

    def set(self, index, value):
        return

    # Converts the index that the user is looking for into the actual new (possibly rotated) index in the array
    def convert(self, index):
        return

    # In order to make this class iterable we have to implement the following method,
    # which uses an iterable object, which implements __init__ and __next__
    # More information here:
    # https://thispointer.com/python-how-to-make-a-class-iterable-create-iterator-class-for-it/
    def __iter__(self):
        return


class CircularArrayIterator:
    def __init__(self):
        return

    # Returns the next value from the array
    def __next__(self):
        return
    # Once there are no items left: raise StopIteration
