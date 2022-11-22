import matplotlib.pyplot as plt
import numpy as np
from wsn import WSN
import networkx as nx
import time

G=nx.Graph()

TOTAL_NODES = 20
AREA = 50
TX_RANGE = 20
BASE = 5

# axis = [(x,y) for x in range(AREA) for y in range(AREA)]
axis = np.random.randint(0, AREA, size=(2, TOTAL_NODES))  
nodes = []
for i in range(TOTAL_NODES):
    node = WSN(i, axis[0][i], axis[1][i])
    nodes.append(node)


axis = np.random.randint(0, AREA, size=(2, TOTAL_NODES))  
nodes = []
for i in range(TOTAL_NODES):
    node = WSN(i, axis[0][i], axis[1][i])
    nodes.append(node)


temp = []
G.add_nodes_from([i for i in range(TOTAL_NODES)])
for i in range(TOTAL_NODES):

    for j in range(TOTAL_NODES):

        if i!=j and nodes[i].dist(nodes[j]) <= TX_RANGE:

            temp.append((i, j))

G.add_edges_from(temp)

# print("Nodes of graph: ")
# print(G.nodes())
# print("Edges of graph: ")
# print(G.edges())
# print("Adjuscent")
# print(list(G.adj[BASE]))


print(nx.is_connected(G))
print(nx.number_connected_components(G))
print(max(nx.connected_components(G), key=len))


nx.draw(G, with_labels=True)
plt.savefig("simple_path.png") # save as png

while True:

    event_nodes = np.random.randint(0, TOTAL_NODES)
    DATA = round(np.random.random(), 1)

    print("\n\n\nEVENT START")

    # source Tx the data
    first = True
    for path in list(nx.dfs_preorder_nodes(G, source=event_nodes)):
        nodes[path].data = DATA
        if first == True:
            nodes[path].status = "SOURCE"
            first=False
        else:
            nodes[path].status = ""



    # base station display dashboard
    nodes[BASE].status = "BASE"
    for i in range(TOTAL_NODES):
        print(nodes[i])
        nodes[i].data = 0

    time.sleep(3)


# plt.show() # display

