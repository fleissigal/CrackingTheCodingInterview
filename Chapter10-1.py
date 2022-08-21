import math


def sortedMerge(A, B, Asize):
    wrIdx = len(A) - 1
    AIdx = Asize - 1
    BIdx = len(B) - 1

    while wrIdx >= 0:
        if AIdx < 0:
            A[wrIdx] = B[BIdx]
            BIdx -= 1
        elif BIdx < 0:
            A[wrIdx] = A[AIdx]
            AIdx -= 1
        elif A[AIdx] > B[BIdx]:
            A[wrIdx] = A[AIdx]
            AIdx -= 1
        elif A[AIdx] <= B[BIdx]:
            A[wrIdx] = B[BIdx]
            BIdx -= 1
        wrIdx -= 1

# According to the solution in the book
def betterSortedMerge(A, B, Asize):
    wrIdx = len(A) - 1
    AIdx = Asize - 1
    BIdx = len(B) - 1

    while BIdx >= 0:
        if AIdx > 0 and A[AIdx] > B[BIdx]:
            A[wrIdx] = A[AIdx]
            AIdx -= 1
        else:
            A[wrIdx] = B[BIdx]
            BIdx -= 1
        wrIdx -= 1


if __name__ == '__main__':
    A = [3, 5, 8, 12, -math.inf, -math.inf, -math.inf, -math.inf]
    B = [4, 9, 15, 17]
    sortedMerge(A, B, 4)
    print(A)

    A = [3, 5, 8, 12, 17, 20, 24, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf]
    B = [4, 9, 15, 17, 21, 22, 23, 24, 29, 34, 39, 44]
    sortedMerge(A, B, 7)
    print(A)

    A = [3, 5, 8, 12, -math.inf, -math.inf, -math.inf, -math.inf]
    B = [4, 9, 15, 17]
    betterSortedMerge(A, B, 4)
    print(A)

    A = [3, 5, 8, 12, 17, 20, 24, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf]
    B = [4, 9, 15, 17, 21, 22, 23, 24, 29, 34, 39, 44]
    betterSortedMerge(A, B, 7)
    print(A)