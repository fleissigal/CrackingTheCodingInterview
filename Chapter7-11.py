"""
Answer to Question 7.11


Following is one option for classes and methods for the file system question.

For the implementation details, we can use a hash table when possible for quick lookup and insert.
We can use chained linked lists.
Alternatively we can store the files in a binary search tree, and then adding or retrieving files
will be done in O(logn) time. We can also think of a graph.

What we will probably also need for the system is a cache, for quick lookup of recently retrieved data.
This can also be implemented via a hash table.
Additionally, we can improve a regular cache by using a distributed cache, which can scale and use multiple networked
machines to store the data as it grows. This is especially useful when there is a high data volume and load.
The network access times have improved and today this is a good solution for a cache.

"""

class Entity:
    name = ""
    parent = ""
    path = ""
    size = 0
    dateCreated = ""

    def getName(self):
        return
    def getParent(self):
        return
    def getPath(self):
        return
    def getSize(self):
        return
    def getDateCreated(self):
        return
    def setName(self, newName):
        return
    def open(self):
        return

class Folder(Entity):
    folders = [] #array of folders
    files = [] #array of files

class File(Entity):
    None

class System:
    folders = [] #array of folders
    files = [] #array of files

    def store(self):
        return
    def retrieve(self):
        return
    def delete(self):
        return
    def getNumFiles(self):
        return
    def getTotalSize(self):
        return

class Cache:
    folders = [] #array of folders
    files = [] #array of files-