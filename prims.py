def prim(graph):
    VT = set([1]) # Initialize the set of tree vertices with any vertex, here 1
    ET = [] # Initialize the set of edges composing the minimum spanning tree
    while len(VT) < len(graph):
        min_weight = float('inf')
        min_edge = None
        for v in VT:
            for u, weight in graph[v]:
                if u not in VT and weight < min_weight:
                    min_weight = weight
                    min_edge = (v, u)
        VT.add(min_edge[1])
        ET.append(min_edge)
    return ET

graph = {
 1: [(2, 4), (4, 8)],
 2: [(1, 4), (3, 3), (4, 1)],
 3: [(2, 3), (4, 7), (6, 8)],
 4: [(1, 8), (6, 3), (3, 7), (2, 1)],
 6: [(4, 3), (3, 8)]
}

# Call the prim function
minimum_spanning_tree = prim(graph)
# Print the minimum spanning tree
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} - {edge[1]}")

#In the function prim we first initialize the vertex set to any vertex ,here we are starting with vertex 1.
#We initialize the edge set(of spanning tree) to empty
#We run a while loop for the condition length of vertex set is less than length of graph dictionary
#Set minimum weight to infinity and minimum edge to none
#We run a for loop for all vertex v in vertex set and run another for loop for the adjacent vertex, weight of the edge in the graph
#if the adjacent vertex is nt there in the vertex set and weight of the edge is less than minimum weight than we update the min weight and min_edge
#The loop iterates until we have all the vertices and have the best min weights
#then we add these edges to edge set of spanning tree and print them

"""
----------------------------------------------------------------------------------------------------
Output:-

Minimum Spanning Tree:
1 - 2
2 - 4
2 - 3
4 - 6
----------------------------------------------------------------------------------------------------
Application:

DNA Sequencing: In bioinformatics, Prim's algorithm can be employed in DNA sequencing to identify the minimum set of DNA fragments required to reconstruct a full genome. By treating DNA fragments as nodes and their overlaps as weights, Prim's algorithm can help in assembling DNA sequences accurately.

Network Design: Prim's algorithm can be used in network design and infrastructure planning. It helps identify the most efficient and cost-effective way to connect multiple nodes in a network while ensuring connectivity and minimizing the total cost of the network.
----------------------------------------------------------------------------------------------------
Time complexity: O(E log|V| )
"""
