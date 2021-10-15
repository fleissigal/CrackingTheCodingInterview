import math
from collections import deque
import Graph


def buildOrder(graph):
    # Setup
    order = deque()
    processNext = deque()
    in_edges = [0 for _ in range(len(graph.adj))]

    # Creating the inbound edge count and the initial processNext
    for node in graph.adj:
        for edge in node:
            in_edges[edge] += 1
    for index, val in enumerate(in_edges):
        if val == 0:
            processNext.append(index)

    # The main part of the function - keep processing processNext and changing the inbound count
    while processNext:
        nextNode = processNext.popleft()
        for edge in graph.adj[nextNode]:
            in_edges[edge] -= 1
            if in_edges[edge] == 0:
                processNext.append(edge)
        order.append(nextNode)

    # Returning the result
    if len(order) == len(graph.adj):
        return order
    else:
        return ValueError

if __name__ == '__main__':
    # Input: Edges in a directed graph
    edges = [Graph.Edge(0, 3),
             Graph.Edge(1, 3),
             Graph.Edge(3, 2),
             Graph.Edge(5, 0), Graph.Edge(5, 1),
             ]

    # Input: No of vertices
    N = 6

    # construct a graph from a given list of edges
    gr = Graph.Graph(edges, N)

    # print adjacency list representation of the graph
    Graph.printGraph(gr)

    print(buildOrder(gr))

    # Input: Edges in a directed graph
    edges_2 = [Graph.Edge(0, 3),
             Graph.Edge(1, 3),
             Graph.Edge(2, 1),
             Graph.Edge(3, 2),
             Graph.Edge(5, 0), Graph.Edge(5, 1),
             ]

    # Input: No of vertices
    N_2 = 6

    # construct a graph from a given list of edges
    gr_2 = Graph.Graph(edges_2, N_2)

    # print adjacency list representation of the graph
    Graph.printGraph(gr_2)

    print(buildOrder(gr_2))