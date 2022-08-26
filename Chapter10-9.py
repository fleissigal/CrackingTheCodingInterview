
def sortedMatrixSearch(matrix, element):
    rows = len(matrix)
    cols = len(matrix[0])

    if rows == 0 or cols == 0:
        return False

    currentElement = matrix[0][cols - 1]

    if currentElement == element:
        return True
    elif currentElement > element:
        if cols == 1:
            return False
        return sortedMatrixSearch([item[:-1] for item in matrix[:]], element)
    else:
        if rows == 1:
            return False
        return sortedMatrixSearch([item[:] for item in matrix[1:]], element)


if __name__ == '__main__':
    matrix = [[0, 0, 2, 5, 6, 7],
              [1, 3, 3, 6, 9, 13],
              [1, 6, 9, 9, 12, 17],
              [5, 8, 12, 15, 18, 20]]

    print(sortedMatrixSearch(matrix, 8))
    print(sortedMatrixSearch(matrix, 2))
    print(sortedMatrixSearch(matrix, 11))
    print(sortedMatrixSearch(matrix, 10))
    print(sortedMatrixSearch(matrix, 7))
    print(sortedMatrixSearch(matrix, 17))
    print(sortedMatrixSearch(matrix, 16))

