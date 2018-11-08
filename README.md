#(c) 2018 William Johnson
#graph-algorithms

Repository meant to contain graph data structures and algorithms. Contains
Vertex, Edge, Graph, and UnDigraph classes with the associated methods and
properties.

external methods:
	aMatrixToGraph

Vertex:
	properties:
		data
	methods:
		__init__
		__str__
		__repr__

Edge:
	properties:
		v1
		v2
		weight
	methods:
		__init__
		flip
		adjustWeight
		__eq__
		__str__
		__repr__

Digraph:
	properties:
		vlist
		elist
	methods:
		__init__
		aMatrix
		is adjacent
		neighbors
		addEdge
		removeEdge
		addVertex
		setEdgeWeight
		removeVertex
		__str__
		__repr__

Graph extends Digaph:
	properties:
		vlist
		elist
	methods:
		__init__
		is adjacent
		neighbors
		addEdge
		removeEdge
		addVertex
		removeVertex
		setEdgeWeight
		aMatrix
		dMatrix
		lMatrix
		__str__
		__repr__

CompleteGraph extends Graph:
	properties:
		vlist
		elist
	methods:
		__init__
		is adjacent
		neighbors
		addEdge
		removeEdge
		addVertex
		removeVertex
		setEdgeWeight
		aMatrix
		dMatrix
		lMatrix
		__str__
		__repr__
