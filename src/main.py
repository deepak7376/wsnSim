import matplotlib.pyplot as plt
import numpy as np
from wsn import WSN
import networkx as nx

G=nx.Graph()

TOTAL_NODES = 10
AREA = 50
TX_RANGE = 20
BASE = 5

# axis = [(x,y) for x in range(AREA) for y in range(AREA)]
axis = np.random.randint(0, AREA, size=(2, TOTAL_NODES))  
nodes = []
for i in range(TOTAL_NODES):
    node = WSN(i, axis[0][i], axis[1][i])
    nodes.append(node)



for i in range(TOTAL_NODES):
    print(nodes[i])

axis = np.random.randint(0, AREA, size=(2, TOTAL_NODES))  
nodes = []
for i in range(TOTAL_NODES):
    node = WSN(i, axis[0][i], axis[1][i])
    nodes.append(node)



for i in range(TOTAL_NODES):
    print(nodes[i])

temp = []
G.add_nodes_from([i for i in range(TOTAL_NODES)])
for i in range(TOTAL_NODES):

    for j in range(TOTAL_NODES):

        if i!=j and nodes[i].dist(nodes[j]) <= TX_RANGE:

            temp.append((i, j))

G.add_edges_from(temp)

# Transfering data from specific node to base node
# node 18 --> node 5
print(list(nx.dfs_edges(G, source=7)))
print(list(nx.dfs_preorder_nodes(G, source=3)))


# print("Nodes of graph: ")
# print(G.nodes())
# print("Edges of graph: ")
# print(G.edges())
# print("Adjuscent")
# print(list(G.adj[BASE]))


# print(nx.is_connected(G))
# print(nx.number_connected_components(G))
# print(max(nx.connected_components(G), key=len))


# nx.draw(G, with_labels=True)
# plt.savefig("simple_path.png") # save as png
# plt.show() # display

