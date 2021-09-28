## Cumulative DivRank
refer : http://www-personal.umich.edu/~qmei/pub/kdd10-divrank.pdf  
for implementation refer the slides file : divRank.pdf  
* algorithm : cum_divrank_numpy.py 
* Graph implemented as Numpy array, hence not the efficient one
* for scalability, Better representation of Graph(dict of dict) will be required  
* NP array provides the benefit of vectorised operations  

  
The paper contains a network, test code for the network is in test_cum_divrank.py .  
To test on own network, edit the edge_dict in file test_cum_divrank.py

