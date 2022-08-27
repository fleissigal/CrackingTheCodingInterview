
def peaksAndValleys(arr):
    if len(arr) <= 2:
        return arr
    nextShouldGoUp = False

    if arr[1] < arr[0]:
        nextShouldGoUp = True

    for i in range(2, len(arr)):
        if (arr[i] > arr[i - 1] and not nextShouldGoUp) or (arr[i] < arr[i - 1] and nextShouldGoUp):
            swap(arr, i, i - 1)
        nextShouldGoUp = not nextShouldGoUp

    return arr

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

if __name__ == '__main__':
    arr = [4, 9, 1, 2, 3, 8, 7, 5]
    print(peaksAndValleys(arr))

    print('\n')

    arr = [5, 3, 1, 2, 3]
    print(peaksAndValleys(arr))

    print('\n')

    arr = [5, 4, 2, 7, 2, 1, 13, 15, 17, 4, 3, 2, 6, 3, 3, 1]
    print(peaksAndValleys(arr))
