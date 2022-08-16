# Origianl question - integers are necessarily distinct

def recursiveMultiply(a, b):
    return auxRecursiveMultiply(max(a, b), min(a, b))

def auxRecursiveMultiply(a, b):
    if b == 1:
        return a
    return a + auxRecursiveMultiply(a, b - 1)


if __name__ == '__main__':

    print(recursiveMultiply(8, 5))
    print(recursiveMultiply(2, 2))
    print(recursiveMultiply(2, 200))
    print(recursiveMultiply(39, 39))
    print(recursiveMultiply(25, 25))
