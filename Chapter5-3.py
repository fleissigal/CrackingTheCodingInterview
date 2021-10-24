def flipBitToWin(num):
    zeroFlag = False
    for i in num:
        if i == '0':
            zeroFlag = True
    if zeroFlag is False:
        return len(num)
    else:
        num = num + "00"

        result = 0
        prevOnes = 0
        currOnes = 0
        zeroFlag = False

        for i in num:
            if i == '1':
                currOnes += 1
                zeroFlag = False
            else:
                if zeroFlag is False:
                    if prevOnes > 0 and currOnes > 0:
                        sum = prevOnes + currOnes + 1
                        if result < sum:
                            result = sum
                    prevOnes = currOnes
                    currOnes = 0
                    zeroFlag = True
                else:
                    if result < prevOnes + 1:
                        result = prevOnes + 1
                    prevOnes = 0
                    currOnes = 0
        return result





if __name__ == '__main__':

    num = "11011101111"
    print(flipBitToWin(num))

    num = "0000000000"
    print(flipBitToWin(num))

    num = "1111111111"
    print(flipBitToWin(num))

    num = "0111111111"
    print(flipBitToWin(num))

    num = "010101010101"
    print(flipBitToWin(num))

    num = "10000000000"
    print(flipBitToWin(num))

    num = "11100111001111"
    print(flipBitToWin(num))

    num = "0"
    print(flipBitToWin(num))

    num = "1"
    print(flipBitToWin(num))

    num = "01"
    print(flipBitToWin(num))