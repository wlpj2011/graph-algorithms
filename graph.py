# (c) 2018 William Johnson
"""Implementation of a data structure to hold a directed graph"""

def aMatrixToGraph(aM):
    v = []
    e = []
    n = len(aM)
    a = list(aM)
    for i in range(n):
        v.append(Vertex(i+1))
    for i in range(n):
        for j in range(n):
            while a[i][j] >= 1:
                e.append(Edge(Vertex(i+1),Vertex(j+1),1))
                a[i][j] -= 1
    return Graph(v,e)
        
class Vertex(object):
    __slots__ = ['_name']

    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __str__(self):
        return '{}'.format(self.name)

    def __repr__(self):
        return 'Vertex({})'.format(self.name)

class Edge(object):
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

    def flip(self):
        return Edge(self.v2,self.v1,self.weight)

    def adjustWeight(self,w):
        self._weight = w

    def __eq__(self,other):
        return (self.v1 == other.v1) and (self.v2 == other.v2) and (self.weight == other.weight)

    def __str__(self):
        return '(({!s},{!s}),weight = {})'.format(self.v1,self.v2,self.weight)

    def __repr__(self):
        return 'Edge({!r},{!r},{})'.format(self.v1,self.v2,self.weight)



class Graph(object):
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
        aMatrix = []
        n = len(self.vlist)
        for _ in range(n):
            aMatrix.append([0]*n)
        for e in self.elist:
            i = e.v1.name
            j = e.v2.name
            aMatrix[i-1][j-1] += 1
        return aMatrix

    def removeVertex(self,v):
        g = self.aMatrix()
        j = v.name
        del g[j]
        for i in range(len(g)):
            del g[i][j]
        self =  aMatrixToGraph(g)
        return self

    def __str__(self):
        return '({!s},{!s})'.format(self.vlist,self.elist)

    def __repr__(self):
        return 'Graph({!r},{!r})'.format(self.vlist,self.elist)

class UnDigraph(Graph):
    __slots__ = ['_vlist','_elist']

    def __init__(self,vlist,elist):
        f = elist.copy()
        for e in f:
            if e.flip() not in f:
                f.append(e.flip())
        super().__init__(vlist,f)

    def aMatrix(self):
        return super().aMatrix()

    def dMatrix(self):
        dMatrix = []
        n = len(self.vlist)
        for _ in range(n):
            dMatrix.append([0]*n)
        for e in self.elist:
            dMatrix[e.v1.name-1][e.v1.name-1] += 0.5
            dMatrix[e.v2.name-1][e.v2.name-1] += 0.5
        for i in range(n):
            for j in range(n):
                dMatrix[i][j] = int(dMatrix[i][j])
        return dMatrix

    def lMatrix(self):
        lMatrix = []
        dMatrix = self.dMatrix()
        aMatrix = self.aMatrix()
        for i in range(len(self.vlist)):
            for j in range(len(self.vlist)):
                lMatrix[i][j] = dMatrix[i][j]-aMatrix[i][j]
        return lMatrix

    def __str__(self):
        return '({!s},{!s})'.format(self.vlist,self.elist)

    def __repr__(self):
        return 'UnDigraph({!r},{!r})'.format(self.vlist,self.elist)
