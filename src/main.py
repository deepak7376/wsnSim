import matplotlib.pyplot as plt
import numpy as np
from wsn import WSN
import networkx as nx
G=nx.Graph()

config ={
    'num_nodes': 50,
    'max_range' :200,
    'sim_time':10,
    'power':10,
    'data':20


}

cor=np.random.randint(config['max_range'], size=(2, config['num_nodes']))
nodes = [WSN(config['power'], i, config['data'], cor[:,i][0], cor[:,i][1]) for i in range(config['num_nodes']) ]



for i in range(config['num_nodes']):
    print(nodes[i])

for i in range(config['num_nodes']):
    for j in range(config['num_nodes']):

        if i!=j and nodes[i].dist(nodes[j])<50:

            G.add_edge(nodes[i],nodes[j])


    
print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())
print("Adjuscent")
print(list(G.adj[nodes[0]]))
nx.draw(G)
plt.savefig("simple_path.png") # save as png
plt.show() # display

