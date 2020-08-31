import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
# G.add_node("a")
# G.add_nodes_from(["b","c"])

G.add_edge(1,2)
edge = (1, "e")
G.add_edge(*edge)
edge = (1, "b")
G.add_edge(*edge)
edge = (2, 'e')
G.add_edge(*edge)

print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(list(G.adj[2])[0])
# nx.draw(G)
# plt.savefig("simple_path.png") # save as png
# plt.show() # display