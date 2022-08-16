
def permWoutDups(str):
    result = []
    auxPermWoutDups(result, "", str.lower())
    return result

def auxPermWoutDups(arr, strBuilt, strLeft):
    if strLeft == '':
        arr.append(strBuilt)
    for i in range(len(strLeft)):
        auxPermWoutDups(arr, strBuilt + strLeft[i], strLeft[:i] + strLeft[(i + 1):])


if __name__ == '__main__':
    print(permWoutDups("ab"))
    print(permWoutDups("abc"))
    print(permWoutDups("bart"))
    print(permWoutDups("brazil"))