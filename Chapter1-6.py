import string

def compressString(s):
    if (len(s) <= 2):
        return s
    else:
        result = ""
        curr_char = s[0]
        curr_count = 1

        for idx in range(len(s)):
            if idx != 0:
                if s[idx] == s[idx - 1]:
                    curr_count += 1
                else:
                    result += curr_char
                    result += str(curr_count)
                    curr_char = s[idx]
                    curr_count = 1
        result += curr_char
        result += str(curr_count)

        if len(result) < len(s):
            return result
        else:
            return s


if __name__ == '__main__':
    print(compressString("aabbbccc"))
    print(compressString("aabcc"))
    print(compressString("abc"))
    print(compressString("a"))
    print(compressString(""))
    print(compressString("aabcccccaaa"))
