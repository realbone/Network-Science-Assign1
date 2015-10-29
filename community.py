import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import community
import operator
from itertools import groupby
from operator import itemgetter


filelist = ['CA-CondMat.txt','RN_1.txt','RN_2.txt','RN_3.txt','RN_4.txt']
# filelist = ['GN_1.txt','GN_2.txt','GN_3.txt','GN_4.txt','GN_5.txt']

for i in range(len(filelist)):

	G = nx.read_edgelist(filelist[i])
	#first compute the best partition
	partition = community.best_partition(G)
	com_keys_list=[]
	com_size_list=[]
	for com in set(partition.values()):
		com_keys = [nodes for nodes in partition.keys() if partition[nodes] == com]
		com_keys_list = com_keys_list + [com_keys]
		com_size_list = com_size_list + [len(com_keys)]

	plt.subplot(3,2,i+1)
	plt.hist(com_size_list,bins=20)
	plt.xlabel('Community Size'+'\navg = '+str(np.mean(com_size_list)) + ',num = '+ str(len(com_size_list)))
	plt.ylabel('Frequency')
	plt.title('RN' + str(i*10) +"%"+ "Shuffled")
	plt.tight_layout()
	print str(i)+" th step finished\n"
	# plt.title('GN ' + str(nx.number_of_nodes(G)) + "Nodes")

plt.show()

