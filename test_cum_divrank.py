import numpy as np
from helpers import Graph
from cum_divrank_numpy import cumDivrank
import os

plot_save_path = 'plots/'
if not os.path.exists(plot_save_path):
    os.makedirs(plot_save_path)


def test_on_graph(edge_dict, image_save_path='cumulative_div_rank.png', pointWiseApprox=False):
    G = Graph(edge_dict=edge_dict, to_directed=False, add_self_loop=True, plot_name=os.path.join(plot_save_path, 'input_graph.png'))

    stat_dist = cumDivrank(G.graph, pointWiseApprox=pointWiseApprox, tol=5e-7, alpha=0.45, d=0.85, max_iter=3000)

    stat_dist = stat_dist.reshape(G.graph.shape[0], )
    # print(stat_dist)
    top = np.argsort(stat_dist)
    top = list(top)
    top.reverse()
    # print(top)
    for index in top:
        print(G._int_to_nodes[index], stat_dist[index])
    G.plot(vertex_weights=stat_dist * 4000, save_path=os.path.join(plot_save_path, image_save_path))


if __name__ == '__main__':
    from graph_input import edges
    # edges = {
    #         1: [2, 3, 6, 7, 8, 9],
    #         2: [1, 3, 10, 11, 12],
    #         3: [1, 2, 15, 16, 17],
    #         4: [11, 13, 14],
    #         5: [17, 18, 19, 20],
    #         6: [1],
    #         7: [1],
    #         8: [1],
    #         9: [1],
    #         10: [2],
    #         11: [2, 4],
    #         12: [2],
    #         13: [4],
    #         14: [4],
    #         15: [3],
    #         16: [3],
    #         17: [3, 5],
    #         18: [5],
    #         19: [5],
    #         20: [5]
    # }
    test_on_graph(edge_dict=edges)
    test_on_graph(edge_dict=edges, image_save_path='pointWise.png', pointWiseApprox=True)
    # print('---test case 2-----')
    #
    # edges = {
    #         1: [2, 3, 4],
    #         2: [1, 3],
    #         3: [1, 2],
    #         4: [1]
    # }
    # test_on_graph(edge_dict=edges, image_save_path='cumulative_div_rank_2.png')
