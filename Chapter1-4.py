import string

NUM_CHARS = 26


def isPalindromePermutation(str):
    array = [0] * NUM_CHARS
    for char in str:
        if char.isalpha():
            char = char.lower()
            idx = string.ascii_lowercase.index(char)
            array[idx] += 1
    oddCount = 0
    for i in array:
        if isOdd(i):
            oddCount += 1
    return oddCount <= 1


def isOdd(num):
    return num % 2 == 1


if __name__ == '__main__':
    print(isPalindromePermutation("Tact Coa"))
    print(isPalindromePermutation(""))
    print(isPalindromePermutation(" "))
    print(isPalindromePermutation("a"))
    print(isPalindromePermutation("%"))
    print(isPalindromePermutation("  "))
    print(isPalindromePermutation("accD *ADB"))
    print(isPalindromePermutation("acc $D ADBg"))
    print(isPalindromePermutation("accD ADBgb"))
    print(isPalindromePermutation("accD AD!Bgb b"))
