def oneWay(s1, s2):
    if s1 == s2:
        return True
    if len(s1) == len(s2):
        if changedLetter(s1, s2):
            return True
    if len(s1) - len(s2) > 1 or len(s2) - len(s1) > 1:
        return False
    else:
        return additionRemovalAux(s1, s2)


def changedLetter(s1, s2):
    diff = 0
    for idx in range(len(s1)):
        if s1[idx] != s2[idx]:
            diff += 1
    return diff == 1


def additionRemovalAux(s1, s2):
    if len(s1) > len(s2):
        return additionRemoval(s1, s2)
    else:
        return additionRemoval(s2, s1)


def additionRemoval(longStr, shortStr):
    for idx in range(len(longStr)):
        if (longStr[:idx] + longStr[(idx + 1):]) == shortStr:
            return True
    return False


if __name__ == '__main__':
    print(oneWay("pale", "ple"))
    print(oneWay("pales", "pale"))
    print(oneWay("pale", "bale"))
    print(oneWay("pales", "bale"))
    print(oneWay("pale", "bake"))
    print(oneWay("bakes", "bake"))
    print(oneWay(" ", " "))
    print(oneWay("", ""))
    print(oneWay("a", "a"))
    print(oneWay("a", "ab"))
    print(oneWay("a", "abc"))
    print(oneWay("ac", "abc"))
