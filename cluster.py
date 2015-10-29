import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import operator

filelist = ['CA-CondMat.txt','RN_1.txt','RN_2.txt','RN_3.txt','RN_4.txt']
# filelist = ['GN_1.txt','GN_2.txt','GN_3.txt','GN_4.txt','GN_5.txt']

avg_list = []

for i in range(len(filelist)):

	G = nx.read_edgelist(filelist[i])
	ccoef = nx.clustering(G)

	plt.subplot(3,2,i+1)
	plt.hist(ccoef.values(),bins = 40)
	plt.xlabel('Clustering Coefficient')
	plt.ylabel('Frequency')
	# plt.title('RN' + str(i*10) +"%"+ "Shuffled")
	plt.tight_layout()

	plt.title('GN ' + str(nx.number_of_nodes(G)) + "Nodes")


	avg_list = avg_list + [np.mean(ccoef.values())]

plt.show()

print avg_list, np.var(avg_list)