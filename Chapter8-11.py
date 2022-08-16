
from enum import IntEnum

class Coin(IntEnum):
    QUARTER = 25
    DIME = 10
    NICKEL = 5
    CENT = 1


def coins(n):
    result = [0]
    auxCoins(0, n, result, Coin.QUARTER)
    return result

def auxCoins(sum, n, result, nextType):
    if sum == n:
        result[0] += 1
        return
    if nextType == 0:
        return
    nextCoin = getNextCoin(nextType)
    for i in range(n // nextType + 1):
        if nextType * i + sum <= n:
            auxCoins(nextType * i + sum, n, result, nextCoin)


def getNextCoin(nextType):
    if nextType == Coin.QUARTER:
        return Coin.DIME
    elif nextType == Coin.DIME:
        return Coin.NICKEL
    elif nextType == Coin.NICKEL:
        return Coin.CENT
    elif nextType == Coin.CENT:
        return 0


if __name__ == '__main__':
    print(coins(2))
    print(coins(5))
    print(coins(7))
    print(coins(10))
    print(coins(50))