import string

NUM_CHARS = 26


def arePermutations(s1, s2):
    if len(s1) != len(s2):
        return False
    array = [0] * NUM_CHARS
    for char in s1:
        idx = string.ascii_lowercase.index(char)
        array[idx] += 1
    for char in s2:
        idx = string.ascii_lowercase.index(char)
        array[idx] -= 1
        if array[idx] < 0:
            return False
    return True


if __name__ == '__main__':
    print(arePermutations("", ""))
    print(arePermutations("a", "a"))
    print(arePermutations("ab", "ba"))
    print(arePermutations("great", "grate"))
    print(arePermutations("abcdef", "abbcdef"))
    print(arePermutations("abcdef", "abbcde"))
    print(arePermutations("galgal", "laggal"))
    print(arePermutations("tnsjflg", "menckfy"))
