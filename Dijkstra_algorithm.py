import numpy as np
from math import inf
import Graphs


def smallest_in(l,e):
    """
    :param l: (list) a list of int not null
    :param e: (list) a list of int
    :return: (int) the index of the smallest int in the list l excepted index in e
    """
    smallest = inf
    index = -1
    for i in range(len(l)):
        if i in e:
            continue
        if l[i] < smallest:
            smallest = l[i]
            index = i
    return index


def Dijkstra_shortest_path(A, start, end):
    """
    :param A: (np.array) adjacency matrix of a graph
    :param start: the start vertice
    :param end: the end vertice
    :return: the length of shortest path from 'start' to 'end'
    """
    size = len(A)
    L = np.arange(size, dtype=float)
    for i in range(size):
        L[i] = inf
    L[start] = 0
    S = []
    while end not in S:
        u = int(smallest_in(L, S))
        S.append(u)
        for v in range(size):
            if v in S:
                continue
            if L[u] + A[u][v] < L[v]:
                L[v] = L[u] + A[u][v]
        print(S)
    return L[end]


if __name__ == '__main__':
    A = Graphs.graph_test
    r = Dijkstra_shortest_path(A, 0, 5)
    print(r)
