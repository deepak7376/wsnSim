from main import G, nodes
import networkx as nx
import time
import numpy as np

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
            nodes[path].status = "hop"



    # base station display dashboard
    nodes[BASE].status = "BASE"
    for i in range(TOTAL_NODES):
        print(nodes[i])
        nodes[i].data = 0

    time.sleep(3)