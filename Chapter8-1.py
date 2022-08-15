
def recursiveTripleStep(n):
    if n >= 0 and n <= 2:
        return n
    if n == 3:
        return 4
    return recursiveTripleStep(n-1) + recursiveTripleStep(n-2) + recursiveTripleStep(n-3)


def memoizationTripleStep(n):
    if n >= 0 and n <= 2:
        return n
    if n == 3:
        return 4
    a = 1
    b = 2
    c = 4
    for i in range(4, n):
        d = a + b + c
        a = b
        b = c
        c = d
    return a + b + c


if __name__ == '__main__':

    print(recursiveTripleStep(1))
    print(recursiveTripleStep(2))
    print(recursiveTripleStep(3))
    print(recursiveTripleStep(4))
    print(recursiveTripleStep(5))
    print(recursiveTripleStep(6))
    print(recursiveTripleStep(7))
    print(recursiveTripleStep(8))
    print(recursiveTripleStep(9))

    print("\n")

    print(memoizationTripleStep(1))
    print(memoizationTripleStep(2))
    print(memoizationTripleStep(3))
    print(memoizationTripleStep(4))
    print(memoizationTripleStep(5))
    print(memoizationTripleStep(6))
    print(memoizationTripleStep(7))
    print(memoizationTripleStep(8))
    print(memoizationTripleStep(9))