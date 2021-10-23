def insertion(N, M, i, j):
    if i > j or i < 0 or j >= 32:
        return 0
    mask = ~(((1 << (j-i+1)) - 1) << i)
    result = N & mask
    M = M << i
    return result | M


if __name__ == '__main__':
    N = int('10000000000', 2)
    M = int('10011', 2)
    result = insertion(N, M, 2, 6)
    print(bin(result))

    N = int('100', 2)
    M = int('01', 2)
    result = insertion(N, M, 1, 2)
    print(bin(result))

    N = int('1001010110011101', 2)
    M = int('10101111', 2)
    result = insertion(N, M, 8, 15)
    print(bin(result))