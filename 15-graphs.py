"""
Graph Practice
Let's discuss a few more definitions that extend on the topics from the last few videos.

Talking about connectivity in a directed graph is a bit more complicated than in an undirected graph. Let's look at some more definitions:

Disconnected
Disconnected graphs are very similar whether the graph's directed or undirected—there is some vertex or group of vertices that have no connection with the rest of the graph.

Weakly Connected
A directed graph is weakly connected when only replacing all of the directed edges with undirected edges can cause it to be connected. Imagine that your graph has several vertices with one outbound edge, meaning an edge that points from it to some other vertex in the graph. There's no way to reach all of those vertices from any other vertex in the graph, but if those edges were changed to be undirected all vertices would be easily accessible.

Connected
Here we only use "connected graph" to refer to undirected graphs. In a connected graph, there is some path between one vertex and every other vertex.

Strongly Connected
Strongly connected directed graphs must have a path from every node and every other node. So, there must be a path from A to B AND B to A.

"""

# edge list and adjacency list are 2-d list
# connections between all nodes (aka edges)
edge_list = [[0,1], [1,2], [1,3], [2,3]]

# index 0 = node 0 and is connected to 1 and one only
adj_list = [[1], [0,2,3], [1,3], [1,2]] 

# adjacency matrix or rectagular array
# index of outer list is the node number and is connected to the index of inner list (the other node number)
adj_matrix = [[0,1,0,0],
              [1,0,1,1],
              [0,1,0,1],
              [0,1,1,0]]