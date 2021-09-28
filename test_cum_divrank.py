import numpy as np
from helpers import Graph
from cum_divrank_numpy import cumDivrank

edges = {
        1: [2, 3, 6, 7, 8, 9],
        2: [1, 3, 10, 11, 12],
        3: [1, 2, 15, 16, 17],
        4: [11, 13, 14],
        5: [17, 18, 19, 20],
        6: [1],
        7: [1],
        8: [1],
        9: [1],
        10: [2],
        11: [2, 4],
        12: [2],
        13: [4],
        14: [4],
        15: [3],
        16: [3],
        17: [3, 5],
        18: [5],
        19: [5],
        20: [5]
    }

G = Graph(edge_dict=edges, to_directed=False, add_self_loop=True)

stat_dist = cumDivrank(G.graph, pointWiseApprox=False)

stat_dist = stat_dist.reshape(G.graph.shape[0],)
# print(stat_dist)
top = np.argsort(stat_dist)
top = list(top)
top.reverse()
# print(top)
for index in top:
    print(G._int_to_nodes[index], stat_dist[index])


stat_dist = cumDivrank(G.graph, pointWiseApprox=True)

stat_dist = stat_dist.reshape(G.graph.shape[0],)
# print(stat_dist)
top = np.argsort(stat_dist)
top = list(top)
top.reverse()
# print(top)
for index in top:
    print(G._int_to_nodes[index], stat_dist[index])