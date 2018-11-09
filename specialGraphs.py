# (c) 2018 William Johnson
"""Holds classes for special types of graphs"""

from graph import *

class CompleteGraph(Graph):
    def __init__(self,n):
        vlist = []
        elist = []
        for v in range(n):
            vlist.append(Vertex(v+1))
        for i in range(n):
            for j in range(i):
                elist.append(Edge(Vertex(i),Vertex(j)))
                elist.append(Edge(Vertex(j),Vertex(i)))
        self._vlist = vlist
        self._elist = elist
