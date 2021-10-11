from collections import deque

import Graph


def dfs(graph, start, end):
    stack = deque()
    visited = []
    stack.append(start)
    while stack:
        next = stack.pop()
        visited.append(next)
        if next == end:
            return True
        else:
            for node in graph.adj[next]:
                if node not in visited:
                    stack.append(node)
    return False


def routeExists(graph, start, end):
    return dfs(graph, start, end)


if __name__ == '__main__':
    # Input: Edges in a directed graph
    edges = [Graph.Edge(1, 4), Graph.Edge(1, 6),
             Graph.Edge(2, 10),
             Graph.Edge(3, 4), Graph.Edge(3, 7), Graph.Edge(3, 9),
             Graph.Edge(4, 5),
             Graph.Edge(5, 2),
             Graph.Edge(6, 3), Graph.Edge(6, 9),
             Graph.Edge(7, 2), Graph.Edge(7, 8),
             Graph.Edge(10, 8),
             ]

    # Input: No of vertices
    N = 11

    # construct a graph from a given list of edges
    gr = Graph.Graph(edges, N)

    # print adjacency list representation of the graph
    Graph.printGraph(gr)

    print(routeExists(gr, 1, 7))
    print(routeExists(gr, 7, 2))
    print(routeExists(gr, 2, 7))
    print(routeExists(gr, 3, 2))
    print(routeExists(gr, 1, 9))
    print(routeExists(gr, 8, 1))