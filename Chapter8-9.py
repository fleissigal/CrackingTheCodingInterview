
def parens(num):
    result = []
    auxParens(result, "", num, 0, 0)
    return result

def auxParens(arr, str, num, open, closed):
    if len(str) == 2 * num:
        arr.append(str)
        return
    if open < num:
        auxParens(arr, str + '(', num, open + 1, closed)
    if open > closed:
        auxParens(arr, str + ')', num, open, closed + 1)


if __name__ == '__main__':
    print(parens(1))
    print(parens(2))
    print(parens(3))
    print(parens(4))