
def sparseSearch(arr, element):
    return auxSparseSearch(arr, element, 0, len(arr) - 1)


def auxSparseSearch(arr, element, left, right):
    mid = (left + right) // 2
    if arr[mid] == element:
        return mid
    if left >= right:
        return -1

    if arr[mid] == '':
        return max(auxSparseSearch(arr, element, mid + 1, right),
                   auxSparseSearch(arr, element, left, mid - 1))

    else:
        if arr[mid] > element:
            if arr[left] != '' and arr[left] > element:
                return -1
            else:
                return auxSparseSearch(arr, element, left, mid - 1)

        else:
            if arr[right] != '' and element > arr[right]:
                return -1
            else:
                return auxSparseSearch(arr, element, mid + 1, right)


if __name__ == '__main__':
    arr = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
    print(sparseSearch(arr, 'ball'))
    print(sparseSearch(arr, 'toy'))
    print(sparseSearch(arr, ''))

    print('\n')

    arr = ['at', '', '', '', 'ball', '', '', '', 'car', '', '', 'dad', '', '', '', '', '', '', '', '', '', '', '',
           'earth', '', '', '', 'fall', 'fell', '', '', '', 'success', '', '', 'toy']
    print(sparseSearch(arr, 'ball'))
    print(sparseSearch(arr, 'success'))
    print(sparseSearch(arr, 'toy'))
    print(sparseSearch(arr, 'prize'))
    print(sparseSearch(arr, 'grey'))
    print(sparseSearch(arr, 'car'))
    print(sparseSearch(arr, ''))
