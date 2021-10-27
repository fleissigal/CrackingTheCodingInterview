def pairwiseSwap(num):
    oddMask = int("AAAAAAAA", 16)
    evenMask = oddMask >> 1

    tmpEvens = (num >> 1) & evenMask
    tmpOdds = (num << 1) & oddMask

    return tmpEvens | tmpOdds


if __name__ == '__main__':
    num = int('1111000011110000', 2)
    print(bin(pairwiseSwap(num)))

    num = int('1001011010010110', 2)
    print(bin(pairwiseSwap(num)))

    num = int('0101010101010101', 2)
    print(bin(pairwiseSwap(num)))

    num = int('1010101010101010', 2)
    print(bin(pairwiseSwap(num)))

    num = int('1001101101010101', 2)
    print(bin(pairwiseSwap(num)))