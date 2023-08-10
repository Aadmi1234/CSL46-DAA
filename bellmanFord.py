def bellmanFord(edgeList, V):
    # Setting the distances of all nodes to infinity
    dist = [1e9] * V

    # Setting the distance of node 'a' to zero
    dist[0] = 0

    # Running the loop for (V-1) times
    for i in range(V-1):
        for edge in edgeList:
            # Edge of the form
            # from_node --> to_node
            (from_node, to_node, weight) = edge

            # Converting alphabets to integers for using as index in list
            u = ord(from_node) - 97
            v = ord(to_node) - 97
            dist[v] = min(dist[v], dist[u]+weight )

    return dist

if __name__ == "__main__":
    # An edge list containing all the edges in the form: (from, to, weight)
    edgeList = [('a','b',-4), ('a','f',-3), ('b','d',-1), ('b','e',-2), ('c','b',8), ('c','f',3), ('d','a',6), ('d','f',4), ('e','c',-3), ('e','f',2)]
    
    # No. of vertices in the graph
    V = 6

    # Function call
    dist = bellmanFord(edgeList, V)

    # To store the characters according to index
    temp = "abcdef"

    print("Distances from a: ")
    for i in range(V):
        print(f"{temp[i]} : {dist[i]}")
        

"""
Output :

Distances from a: 
a : 0
b : -4
c : -9
d : -5
e : -6
f : -6
"""

"""
Time Complexity : O(V * E)
V -> no. of nodes
E -> no. of edges
"""
