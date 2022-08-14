"""
Answer to Question 7.3
"""

from collections import deque
from enum import Enum

class Display:
    currPage = "" #page object

    def showPage(self):
        return
    def turnPageForward(self):
        return
    def turnPageBackward(self):
        return

class Reader:
    bookmarks = [] #array of bookmarks
    username = ""
    name = ""
    savedBooks = [] #array of books
    readBooks = [] #array of books already read

    def markRead(self):
        return
    def setBookmark(self):
        return
    def saveBook(self):
        return
    def getBookmarks(self):
        return
    def removeFromSaved(self):
        return

class Book:
    title = ""
    author = ""
    year = ""
    pages = [] #array of page objects

class Library:
    collection = [] #array of books
    users = [] #array of readers

#     We could have created a separate UserManager object that handles user management

    def addBook(self):
        return
    def removeBook(self):
        return
    def addReader(self):
        return
    def removeReader(self):
        return
    def findBook(self):
        return

class Page:
    text = "" #the page's text

class Bookmark:
    book = "" #book object
    page = "" #page object

    def getBook(self):
        return
    def setBook(self):
        return
    def getPage(self):
        return
    def setPage(self):
        return











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