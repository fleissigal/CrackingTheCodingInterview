# Implementation taken from https://www.techiedelight.com/graph-implementation-python/
# Using this only to focus on the questions


# A class to store a graph edge
class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest


# A class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, N):
        # allocate memory for the adjacency list
        self.adj = [[] for _ in range(N)]

        # add edges to the undirected graph
        for current in edges:
            # allocate node in adjacency list from src to dest
            self.adj[current.src].append(current.dest)


# Function to print adjacency list representation of a graph
def printGraph(graph):
    for src in range(len(graph.adj)):
        # print current vertex and all its neighboring vertices
        for dest in graph.adj[src]:
            print(f"({src} —> {dest}) ", end="")
        print()