# (c) 2018 William Johnson
"""Holds helper functions for graph.py
"""

__all__ = ['aMatrixToGraph']


def aMatrixToGraph(aM):
    """
    Function that takes an adjancecy matrix and converts it to a graph.
    >>> aMatrixToGraph([[0]])
    Graph([Vertex(1)],[])
    >>> aMatrixToGraph([[0,1],[1,0]])
    Graph([Vertex(1), Vertex(2)],[Edge(Vertex(1),Vertex(2),1), Edge(Vertex(2),Vertex(1),1)])
    """
    v = []
    e = []
    n = len(aM)
    a = [l.copy() for l in aM]
    for i in range(n):
        v.append(Vertex(i+1))
    for i in range(n):
        for j in range(n):
            while a[i][j] >= 1:
                e.append(Edge(Vertex(i+1),Vertex(j+1),1))
                a[i][j] -= 1
    return Graph(v,e)
