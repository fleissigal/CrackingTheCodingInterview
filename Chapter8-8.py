
def permutationsWithoutDups(s):
    result = set()
    tempString = ""
    auxPermWithoutDups(s, tempString, result)
    return result

def auxPermWithoutDups(str, tmp, res):
    if str == "":
        res.add(tmp)
        return

    for i in range(len(str)):
        tmp += str[i]
        auxPermWithoutDups(str[:i] + str[i+1:], tmp, res)
        tmp = tmp[:-1]


if __name__ == '__main__':
    s = ""
    print(permutationsWithoutDups(s))
    s = "a"
    print(permutationsWithoutDups(s))
    s = "ab"
    print(permutationsWithoutDups(s))
    s = "abc"
    print(permutationsWithoutDups(s))
    s = "abcc"
    print(permutationsWithoutDups(s))
    s = "abcd"
    print(permutationsWithoutDups(s))
