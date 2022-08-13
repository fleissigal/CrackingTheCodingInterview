def getNext(n):

    c0 = 0
    c1 = 0
    curr = n
    while curr & 1 == 0 and curr != 0:
        c0 += 1
        curr >>= 1
    while curr & 1 == 1:
        c1 += 1
        curr >>= 1
    if c0 + c1 == 8 or c0 + c1 == 0:
        return -1

    flipBit = 1 << (c0 + c1)
    n = n | flipBit

    mask = ~((1 << (c0 + c1)) - 1)
    onesSeq = (1 << (c1 - 1)) - 1

    return (mask & n) | onesSeq

def getPrevious(n):

    c0 = 0
    c1 = 0
    curr = n
    while curr & 1 == 1:
        c1 += 1
        curr >>= 1
    while curr & 1 == 0 and curr != 0:
        c0 += 1
        curr >>= 1
    if c0 + c1 == 8 or c0 + c1 == 0:
        return -1

    flipBit = ~(1 << (c0 + c1))
    n = n & flipBit

    mask = ~((1 << (c0 + c1)) - 1)
    onesSeq = ((1 << (c1 + 1)) - 1) << (c0 - 1)

    return (mask & n) | onesSeq


if __name__ == '__main__':
    N = int('00101010', 2)
    print(getNext(N))

    N = int('00101000', 2)
    print(getNext(N))

    N = int('11111111', 2)
    print(getNext(N))

    N = int('11000000', 2)
    print(getNext(N))

    N = int('11011001111100', 2)
    print(getNext(N))

    print("\n")

    N = int('00101010', 2)
    print(getPrevious(N))

    N = int('00101000', 2)
    print(getPrevious(N))

    N = int('11111111', 2)
    print(getPrevious(N))

    N = int('11000000', 2)
    print(getPrevious(N))

    N = int('10011110000011', 2)
    print(getPrevious(N))