def URLify(str, size):
    sp = countSpaces(str, size)
    for idx in reversed(range(size)):
        if str[idx] != ' ':
            str[idx + sp * 2] = str[idx]
        else:
            str[idx + sp * 2] = '0'
            str[idx + sp * 2 - 1] = '2'
            str[idx + sp * 2 - 2] = '%'
            sp -= 1
    return str


def countSpaces(str, size):
    res = 0
    for idx in range(size):
        if str[idx] == ' ':
            res += 1
    return res


if __name__ == '__main__':
    original = "Mr John Smith    "
    str = []
    for char in original:
        str.append(char)
    size = 13

    print(URLify(str, size))

    original = ""
    str = []
    for char in original:
        str.append(char)
    size = 0

    print(URLify(str, size))

    original = "   "
    str = []
    for char in original:
        str.append(char)
    size = 1

    print(URLify(str, size))

    original = "CTCI is great !      "
    str = []
    for char in original:
        str.append(char)
    size = 15

    print(URLify(str, size))
