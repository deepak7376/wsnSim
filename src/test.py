import networkx as nx
import matplotlib.pyplot as plt

# G=nx.path_graph(4)
G = nx.path_graph(4)
pos = nx.planar_layout(G)
print(pos)
# print(list(nx.dfs_edges(G, source=0)))

# print(list(nx.dfs_edges(G, source=0, depth_limit=2)))

# # import numpy as np
# # a = np.random.randint(0, 3, size=(10, 10))
# # print(a)
# # G = nx.DiGraph(a)

# print("Nodes of graph: ")
# print(G.nodes())
# print("Edges of graph: ")
# print(G.edges())
nx.draw(G, with_labels=True)
plt.savefig("path_graph1.png")
plt.show()