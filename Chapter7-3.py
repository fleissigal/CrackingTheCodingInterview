"""
Answer to Question 7.3
"""

from collections import deque
from enum import Enum

class Song:
    duration = ""
    artist = ""
    title = ""

    def playSong(self):
        return

class Juke:
    collection = [] #array of songs
    playlist = deque() #queue of songs
    payments = [] #array og payments

    def getPayments(self):
        return
    def getNextSong(self):
        return
    def searchSong(self):
        return

class Payment:
    amount = 0

class User:
    name = ""
    payments = [] #array of payments

    def shuffle(self):
        return
    def addSong(self):
        return
    def makePayment(self):
        return
    def deleteSong(self):
        return

class Display:
    playing = "" #current song playing

    def showSong(self):
        return