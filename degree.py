import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


# filelist = ['CA-CondMat.txt','RN_1.txt','RN_2.txt','RN_3.txt','RN_4.txt']
avg_list = []
filelist = ['GN_1.txt','GN_2.txt','GN_3.txt','GN_4.txt','GN_5.txt']
for i in range(len(filelist)):

	G = nx.read_edgelist(filelist[i])
	deg_distribution = nx.degree_histogram(G)

	deg_cdf = [sum(deg_distribution[0:j]) for j in range(len(deg_distribution))]
	plt.subplot(3,2,i+1)
	plt.plot(deg_cdf,'b-', marker = 'o')
	plt.tight_layout()
	# plt.title('RN' + str(i*10) +"%"+ "Shuffled")
	plt.title('GN ' + str(nx.number_of_nodes(G)) + "Nodes")
	plt.ylabel("Frequency")
	plt.xlabel("Node Degree")
	avg_list = avg_list + [np.mean((G.degree()).values())]

print avg_list
print np.var(avg_list)

plt.show()
