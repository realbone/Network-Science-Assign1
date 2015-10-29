import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import operator



def dist(dict):

	keys_list = []
	size_list = []
	for label in set(dict.values()):
		label_keys = [keys for keys in dict.keys() if dict[keys] == label]
		keys_list = keys_list + [label_keys]
		size_list = size_list + [len(label_keys)]

	return size_list




filelist = ['CA-CondMat.txt','RN_1.txt','RN_2.txt','RN_3.txt','RN_4.txt']

# filelist = ['GN_1.txt','GN_2.txt','GN_3.txt','GN_4.txt','GN_5.txt']
avg_list_max=[]
avg_list_min=[]

for i in range(len(filelist)):

	G = nx.read_edgelist(filelist[i])
	degrees = G.degree()
	max_deg_node = max(degrees.iteritems(), key=operator.itemgetter(1))[0]
	min_deg_node = min(degrees.iteritems(), key=operator.itemgetter(1))[0]

	max_deg_spl = nx.single_source_shortest_path_length(G, max_deg_node)
	min_deg_spl = nx.single_source_shortest_path_length(G, min_deg_node)

	avg_list_max += [np.mean(max_deg_spl.values())]
	avg_list_min += [np.mean(min_deg_spl.values())]
	plt.subplot(3,2,i+1)
	plt.plot(dist(max_deg_spl),'b-', marker='o',label = 'L')
	plt.plot(dist(min_deg_spl),'r-', marker='o',label = 'S')
	plt.legend()
	plt.xlabel('shortest path length')
	plt.ylabel('frequency')
	# plt.title('RN' + str(i*10) +"%"+ "Shuffled")
	plt.tight_layout()

	plt.title('GN ' + str(nx.number_of_nodes(G)) + "Nodes")
plt.show()

print avg_list_min, np.var(avg_list_min)
print avg_list_max, np.var(avg_list_max)
