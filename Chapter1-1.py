def hasAllUniqueChars(str):
    ht = {}
    for char in str:
        if char in ht:
            return False
        else:
            ht[char] = 1
    return True


if __name__ == '__main__':
    print(hasAllUniqueChars(""))
    print(hasAllUniqueChars("b"))
    print(hasAllUniqueChars("aa"))
    print(hasAllUniqueChars("authorization"))
    print(hasAllUniqueChars("authorize"))
