class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def printSolution(self, dist):
		print("Vertex \t Distance from Source")
		for node in range(self.V):
			print(node+1, "\t\t", dist[node])

	# A utility function to find the vertex with
	# minimum distance value, from the set of vertices
	# not yet included in shortest path tree
	def minDistance(self, dist, sptSet):

		# Initialize minimum distance for next node
		min = 1e7

		# Search nearest vertex not in the shortest path tree
		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v

		return min_index

	# Function that implements Dijkstra's single source
	# shortest path algorithm for a graph represented
	# using adjacency matrix representation
	def dijkstra(self, src):

		dist = [1e7] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):

			# Pick the minimum distance vertex from
			# the set of vertices not yet processed.
			# u is always equal to src in first iteration
			u = self.minDistance(dist, sptSet)

			# Put the minimum distance vertex in the
			# shortest path tree
			sptSet[u] = True

			# Update dist value of the adjacent vertices
			# of the picked vertex only if the current
			# distance is greater than new distance and
			# the vertex in not in the shortest path tree
			for v in range(self.V):
				if (self.graph[u][v] > 0 and
				sptSet[v] == False and
				dist[v] > dist[u] + self.graph[u][v]):
					dist[v] = dist[u] + self.graph[u][v]

		self.printSolution(dist)

# Driver program
g = Graph(5)
g.graph = [[0,10,0,0,100],
		   [10,0,50,0,0],
		   [0,50,0,20,10],
		   [0,0,20,0,60],
		   [100,0,10,60,0]
		]

g.dijkstra(0)

"""
------------------------------------
Output:
Vertex 	 Distance from Source
1 		 0
2 		 10
3 		 60
4 		 80
5 		 70
------------------------------------
TIME COMPLEXITY:
has a time complexity of O(V^2) using the adjacency matrix representation of graph. The time complexity can be reduced to O((V+E)logV) using adjacency list representation of graph, where E is the number of edges in the graph and V is the number of vertices in the graph.
-------------------------
APPLICATION:
1. Digital Mapping Services in Google Maps
2. Social Networking Applications
3. Telephone Network
_________________________________________________________________________________
"""
