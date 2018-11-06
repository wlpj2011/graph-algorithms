#(c) 2018 William Johnson
#graph-algorithms

Repository meant to contain graph data structures and algorithms. Contains
Vertex, Edge, Graph, and UnDigraph classes with the associated methods and
properties.

Vertex:
	properties:
		name
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

Graph:
	properties:
		vlist
		elist
	methods:
		__init__
		aMatrix
		removeVertex
		__str__
		__repr__

UnDigraph extends Graph:
	properties:
		vlist
		elist
	methods:
		__init__
		removeVertex
		aMatrix
		dMatrix
		lMatrix
		__str__
		__repr__
		