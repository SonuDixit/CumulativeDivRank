import numpy as np

class Graph():
    def __init__(self, edge_dict, to_directed=False, add_self_loop=True ):
        '''
        Args:
            edge_dict: adjacency list format
            to_directed:
            add_self_loop:
        '''
        self._nodes = [k for k in edge_dict.keys()]
        self._int_to_nodes = {i:self._nodes[i] for i in range(len(self._nodes))}
        self._nodes_to_int = {v:k for k,v in self._int_to_nodes.items()}
        self._build_graph(edge_dict=edge_dict, add_self_loop=add_self_loop, to_directed=to_directed)

    def _build_graph(self, edge_dict, add_self_loop=True, to_directed=True):
        '''
        modify this implementation if the weight is being passed
        Args:
            edge_dict:
            add_self_loop:
            to_directed:
        Returns:

        '''
        self.graph = np.zeros((len(self._nodes), len(self._nodes)))
        for node in edge_dict:
            for neighbor in edge_dict[node]:
                self.graph[self._nodes_to_int[node], self._nodes_to_int[neighbor]] = 1.0 # modify here if the weight is being passed

        if to_directed:
            '''
            '''
            self.graph = self.graph+self.graph.T
            self.graph[self.graph>1.0] = 1.0

        if add_self_loop:
            for i in range(self.graph.shape[0]):
                self.graph[i,i]=1.0

    def plot(self, vertex_weights, save_path):
        '''
        Args:
            vertex_weights: required for node size in image [np array, list, or dict{id:size}]
            save_path:

        Returns:

        '''
        import networkx as nx
        import matplotlib.pyplot as plt
        graph = nx.from_numpy_array(self.graph, create_using=nx.DiGraph)
        nx.draw_circular(graph, node_size=vertex_weights, with_labels=True)
        plt.savefig(save_path)
        pass
