# Origianl question - integers are necessarily distinct

def distinctMagicIndex(array):
    if len(array) == 0:
        return "Not found"
    return auxDistinctMagicIndex(array, 0, len(array) - 1)

def auxDistinctMagicIndex(array, left, right):
    if right < left:
        return "Not found"
    idx = (left + right) // 2

    if array[idx] == idx:
        return idx
    if array[idx] > idx:
        return auxDistinctMagicIndex(array, left, idx - 1)
    else:
        return auxDistinctMagicIndex(array, idx + 1, right)


# Followup - integers are not necessarily distinct

def nondistinctMagicIndex(array):
    if len(array) == 0:
        return "Not found"
    return auxNondistinctMagicIndex(array, 0, len(array) - 1)

def auxNondistinctMagicIndex(array, left, right):
    if right < left:
        return "Not found"
    idx = (left + right) // 2

    if array[idx] == idx:
        return idx
    # We possibly check both halves of the array. If we didn't find it in the left side - we return result from the right side
    valFromLeftSide = auxNondistinctMagicIndex(array, left, min(idx - 1, array[idx]))
    if valFromLeftSide != "Not found":
        return valFromLeftSide
    else:
        return auxNondistinctMagicIndex(array, max(idx + 1, array[idx]), right)


if __name__ == '__main__':

    print(distinctMagicIndex([0, 2, 4, 7, 9]))
    print(distinctMagicIndex([0, 1, 2, 3, 4, 5]))
    print(distinctMagicIndex([-3, -2, 1, 2, 4]))
    print(distinctMagicIndex([-3, -2, 1, 2, 4, 9, 11]))
    print(distinctMagicIndex([-5, -3, -1, 1, 3, 4, 6, 10]))
    print(distinctMagicIndex([-5, -3, -1, 1, 3, 4, 5, 7]))
    print(distinctMagicIndex([-5, -3, -1, 1, 3, 4, 5, 10]))
    print(distinctMagicIndex([-3, 1, 4, 6, 7, 8, 11, 15]))

    print("\n")

    print(nondistinctMagicIndex([-3, -1, 2, 2, 2, 6, 7]))
    print(nondistinctMagicIndex([-10, -5, 2, 2, 2, 3, 4, 5, 9, 12, 13]))
    print(nondistinctMagicIndex([-5, -4, -3, -2, -1, 0]))
