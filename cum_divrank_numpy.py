import numpy as np

def cumDivrank(G, alpha=0.25, d=0.85, max_iter=400, tol=1.0e-5, pi_0 = None, prefer = None, pointWiseApprox=False):
    '''
    Args:
        G: directed graph (np array of size nxn)
        alpha: 1-alpha is strength of self connection
        d: dampaning factor
        max_iter:
        tol:
        pi_0: initial state distribution , np array shape= nx1
        prefer: personalised state preference distribution, np array shape= nx1

        pointWiseApprox : if True, it approximates N_T(V) using only previous step probs , referred as pointWiseDivRank in Paper
    Returns:

    '''
    assert G.shape[0]==G.shape[1]
    assert np.prod((G>=0.0))==1.0, 'all weights should be non negative'

    G = G / np.reshape(np.sum(G, axis=1),(-1,1))
    G = G * alpha
    for i in range(G.shape[0]):
        G[i][i] = 1-alpha

    if pi_0 is None:
        x = np.ones((G.shape[0],1)) * 1/G.shape[0] # initialise p_0(u) = 1/N for all u
    else:
        assert np.prod((pi_0>=0))==1.0, 'pi_0 should have non negative vals'
        assert np.sum(pi_0)==1.0, 'pi_0 should be a distribution'
        x = pi_0.reshape((G.shape[0],1))
    if prefer is None:
        p_star = np.ones((G.shape[0],1)) * 1/G.shape[0]
    else:
        assert np.prod((prefer>0)==1.0), 'prefer should have non negative vals'
        assert np.sum(prefer)==1.0, 'prefer should be a distribution'
        p_star = prefer.reshape((G.shape[0],1))

    '''
    p_star : personalisation state distribution
    x : initial state distribution
    '''
    visits = [] # T x n
    visits.append(x)
    x_prev = x

    for iteration in range(max_iter):
        if pointWiseApprox:
            _norm_val = np.array(visits[-1:]).sum(axis=0)
        else:
            _norm_val = np.array(visits).sum(axis=0)
        _norm_val = _norm_val/np.sum(_norm_val)

        out_degree = G @ _norm_val # nx1

        G_new = (1-d)*p_star.reshape(1,-1) + (d * (G * _norm_val.reshape(1,-1))/ out_degree)

        x_next = (x_prev.T @ G_new).T # nx1
        # abs value compare
        error = np.sum(np.abs(x_next-x_prev))
        # print('error:', error)
        if error < x_prev.shape[0] * tol:
            print('converged at iteration:', iteration)
            return x_next

        x_prev = x_next
        visits.append(x_next)

    print('could not converge')



if __name__ == '__main__':
    # network in the paper
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

    graph = np.zeros((20,20), np.float)
    for u, vs in edges.items():
        for v in vs:
            # g.add_edge(u, v)
            graph[u-1,v-1] = 1.0
            graph[v-1,u-1] = 1.0

    stat_dist = cumDivrank(graph)

    stat_dist = stat_dist.reshape(graph.shape[0],)
    # print(stat_dist)
    top = np.argsort(stat_dist)
    top = list(top)
    top.reverse()
    print(top)
    for index in top:
        print(index+1, stat_dist[index])

