"""
Answer to Question 7.1
"""

from collections import deque
from enum import Enum

class Suit(Enum):
    CLUBS = 1
    HEARTS = 2
    SPADES = 3
    DIAMONDS = 4

class Card:
    suit = 1
    num = 0

    def getSuit(self):
        return
    def getNum(self):
        return

class Deck:
    deck = deque()

    def dealHand(self):
        return
    def shuffle(self):
        return
    def getCard(self):
        return
    def addCard(self):
        return
    def getSize(self):
        return

class Hand:
    hand = [] #array of cards


### Blackjack part

class Player:
    name = ""
    hand = []

    def requestCard(self):
        return

class Dealer(Player):
    name = ""

class Nondealer(Player):
    name = ""

class BlackjackHand(Hand):
    score = 0

    def getScore(self):
        return

class Round:
    round = [] #array of players

    def addPlayer(self):
        return

    def dealCards(self):
        return

    def calcScores(self):
        return

    def addScoresToBoard(self):
        return

class Scoreboard():
    scores = [] #array of players with their scores

class Game:
    game = [] #array of rounds
    scoreboard = Scoreboard()

    def startNewRound(self):
        return

    def getWinner(self):
        return
