import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

filename = "CA-CondMat.txt"

RN = nx.read_edgelist(filename)

n_RN = nx.number_of_edges(RN)

RN_list = [RN]
for i in range(4):
	RN_list.append(nx.double_edge_swap(RN.copy(), nswap = int(n_RN*(i+1)*0.1), max_tries = 2*(i+1)*n_RN))
	nx.write_edgelist(RN_list[i],'RN_' + str(i+1) + '.txt', data = False)

nn_RN = nx.number_of_nodes(RN)

avg_deg_of_node = np.mean((RN.degree()).values())

GN_list = []
for i in range(5):
	GN_list.append(nx.barabasi_albert_graph(nn_RN+1000*i, int(avg_deg_of_node)))
	nx.write_edgelist(GN_list[i],'GN_'+str(i+1)+'.txt', data = False)
	

