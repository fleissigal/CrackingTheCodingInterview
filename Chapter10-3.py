
def searchInRotatedArray(arr, element):
    idx = auxSearchInRotatedArray(arr, element, 0, len(arr) - 1)
    return idx


def auxSearchInRotatedArray(arr, element, left, right):
    mid = (left + right) // 2
    if arr[mid] == element:
        return mid
    if left >= right:
        return -1

    if arr[mid] < arr[right]:
        if arr[mid] < element <= arr[right]:
            return auxSearchInRotatedArray(arr, element, mid + 1, right)
        else:
            return auxSearchInRotatedArray(arr, element, left, mid - 1)

    if arr[mid] > arr[left]:
        if arr[left] <= element < arr[mid]:
            return auxSearchInRotatedArray(arr, element, left, mid - 1)
        else:
            return auxSearchInRotatedArray(arr, element, mid + 1, right)

    # This code is for the case of duplicated elements
    if arr[mid] == arr[left] and arr[mid] == arr[right]:
        return max(auxSearchInRotatedArray(arr, element, mid + 1, right),
                   auxSearchInRotatedArray(arr, element, left, mid - 1))
    if arr[left] == arr[mid]:
        return auxSearchInRotatedArray(arr, element, mid + 1, right)
    if arr[mid] == arr[right]:
        return auxSearchInRotatedArray(arr, element, left, mid - 1)

if __name__ == '__main__':
    arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    print(searchInRotatedArray(arr, 5))

    arr = [10, 14, 15, 16, 19, 20, 25, 1, 3, 4, 5, 7]
    print(searchInRotatedArray(arr, 5))

    arr = [4, 5, 7, 10, 14, 15, 16, 19, 20, 25, 1, 3]
    print(searchInRotatedArray(arr, 5))

    arr = [70, 75, 17, 18, 30, 31, 35, 50, 60]
    print(searchInRotatedArray(arr, 18))

    arr = [24, 25, 26, 27, 30, 31, 13, 18, 23]
    print(searchInRotatedArray(arr, 18))

    arr = [30, 30, 30, 30, 30, 31, 13, 18, 30]
    print(searchInRotatedArray(arr, 18))

    arr = [30, 30, 30, 30, 30, 31, 13, 18, 21]
    print(searchInRotatedArray(arr, 18))

    arr = [12, 18, 21, 30, 30, 30, 30, 30, 30]
    print(searchInRotatedArray(arr, 18))

    arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1]
    print(searchInRotatedArray(arr, 2))