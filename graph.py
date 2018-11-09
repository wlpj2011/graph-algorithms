# (c) 2018 William Johnson
"""Implementation of a data structure to hold a directed graph"""

from helper import *

__all__ = ['Vertex','Edge','Digraph','Graph']
        
class Vertex(object):
    """
    Class that is used to define vertices of graphs. Only distinguishing
    property of vertices is their name.
    """
    __slots__ = ['_data']

    def __init__(self,data):
        self._data = data

    @property
    def data(self):
        return self._data

    def __str__(self):
        return '{}'.format(self.data)

    def __repr__(self):
        return 'Vertex({})'.format(self.data)

class Edge(object):
    """
    Class used to define the Edges of graphs. Each edge is directed and
    potentially weighted. The edge goes from the first vertex to the second
    vertex.
    Edges are initialized with a weight of 1 if no weight is given.
    """
    __slots__ = ['_vtup','_weight']

    def __init__(self,v1,v2,weight = 1):
        self._vtup = (v1,v2)
        self._weight = weight

    @property
    def weight(self):
        return self._weight

    @property
    def v1(self):
        return self._vtup[0]

    @property
    def v2(self):
        return self._vtup[1]

    @weight.setter
    def weight(self,w):
        self._weight = w

    def _flip(self):
        """
        Given an edge, flip make the edge going in the opposite direction with
        the same weight.
        """
        return Edge(self.v2,self.v1,self.weight)

    def __eq__(self,other):
        return (self.v1 == other.v1) and (self.v2 == other.v2) and (self.weight == other.weight)

    def __str__(self):
        return '(({!s},{!s}),weight = {})'.format(self.v1,self.v2,self.weight)

    def __repr__(self):
        return 'Edge({!r},{!r},{})'.format(self.v1,self.v2,self.weight)

class Digraph(object):
    """
    Data structure to hold a mathematical directed Graph. Takes a list of
    vertices and a list of edges.
    """
    __slots__ = ['_vlist','_elist']

    def __init__(self,vlist,elist):
        self._vlist = vlist
        self._elist = elist

    @property
    def vlist(self):
        return self._vlist

    @property
    def elist(self):
        return self._elist
    
    def aMatrix(self):
        """
        Creates the adjacency matrix of a graph. The matrix with 1 in the i,j
        position if there is an edge going from the ith vertex to the 
        jth vertex.
        """
        aMatrix = []
        n = len(self.vlist)
        for _ in range(n):
            aMatrix.append([0]*n)
        for e in self.elist:
            i = e.v1.data
            j = e.v2.data
            aMatrix[i-1][j-1] += 1
        return aMatrix

    def isAdjacent(self,v1,v2):
        """
        Returns true if there is an edge going from v1 to v2.
        """
        return Edge(v1,v2) in self.elist

    def neighbors(self,v1):
        """
        Returns a list of the neighbors of a given vertex of a digraph.
        """
        neighbors = {}
        for e in self.elist:
            if v1 == e.v1:
                neighbors.add(e.v2)
        return list(neighbors)

    def addEdge(self,e):
        """Add an edge e to the graph"""
        self.elist.append(e)
        
    def removeEdge(self,e):
        """Remove an edge e from the graph"""
        self.elist.remove(e)

    def addVertex(self):
        """Adds a vertex to the graph with no connections"""
        n = len(self.vlist)
        self.vlist.append(Vertex(n+1))
    
    def setEdgeWeight(self,e,w):
        """Sets the edgeweight of an edge"""
        self.elist.remove(e)
        e.weight(w)
        self.elist.append(e)

    def removeVertex(self,v):
        """
        Removes a given vertex from a graph, this also removes the edges
        connected to that vertex and renumbers the vertices so there
        isn't a gap.
        """
        g = self.aMatrix()
        j = v.data
        del g[j]
        for i in range(len(g)):
            del g[i][j]
        self =  aMatrixToGraph(g)
        return self

    def __str__(self):
        return '({!s},{!s})'.format(self.vlist,self.elist)

    def __repr__(self):
        return 'Digraph({!r},{!r})'.format(self.vlist,self.elist)

class Graph(Digraph):
    """
    Class that extends graph but is meant specifically for undirected graphs.
    If given a nonsymmetric edge list, it will add the edges necessary for it
    to be symmetric.
    """
    __slots__ = ['_vlist','_elist']

    def __init__(self,vlist,elist):
        f = elist.copy()
        for e in f:
            if e._flip() not in f:
                f.append(e._flip())
        super().__init__(vlist,f)

    def aMatrix(self):
        return super().aMatrix()

    def dMatrix(self):
        """
        Return the degree Matrix of a graph. That is a matrix with the number
        of edges connected to Vertex i as the i,ith entry of the matrix and 
        0 everywhere else.
        """
        dMatrix = []
        n = len(self.vlist)
        for _ in range(n):
            dMatrix.append([0]*n)
        for e in self.elist:
            dMatrix[e.v1.data-1][e.v1.data-1] += 0.5
            dMatrix[e.v2.data-1][e.v2.data-1] += 0.5
        for i in range(n):
            for j in range(n):
                dMatrix[i][j] = int(dMatrix[i][j])
        return dMatrix

    def lMatrix(self):
        """
        Returns the laplacian matrix of a graph. That is the degree matrix
        minus the adjacency matrix.
        """
        n = len(self.vlist)
        lMatrix = []
        dMatrix = self.dMatrix()
        aMatrix = self.aMatrix()
        for _ in range(n):
            lMatrix.append([0]*n)
        for i in range(n):
            for j in range(n):
                lMatrix[i][j] = dMatrix[i][j]-aMatrix[i][j]
        return lMatrix

    def __str__(self):
        return '({!s},{!s})'.format(self.vlist,self.elist)

    def __repr__(self):
        return 'Graph({!r},{!r})'.format(self.vlist,self.elist)


if __name__ == '__main__':
    from doctest import testmod
    testmod()
