import pandas as pd 
import networkx as nx 
import numpy as np 
import matplotlib.pyplot as plt 

def readEdgeList(filename):
	edge_list = pd.read_csv(filename)
	shape = edge_list.shape
	if shape[1] != 2:
		print "There is an error in the file- more than 2 columns exist."
		return edge_list[:1]
	return edge_list

def degree(edgeList, in_or_out):
	if in_or_out == "in":
		degree = edgeList['1'].value_counts()
	elif in_or_out == "out":
		degree = edgeList['0'].value_counts()
	return degree

def combineEdgeLists(edgeList1, edgeList2):
	both_lists = [edgeList1, edgeList2]
	combined = pd.concat(both_lists)
	combined = combined.drop_duplicates()
	return combined

def pandasToNetworkX(edgeList):
	g= nx.DiGraph()
	for x, y in edgeList.to_records(index=False):
		g.add_edge(x,y)
	return g

def randomCentralNode(inputDiGraph):
	eigenCenter = nx.eigenvector_centrality(inputDiGraph)
	center_sum = 0
	#print eigenCenter['1zrBQvkTNhFFby4V5UiK2L']
	for k,v in eigenCenter.items():
		center_sum = center_sum + v 
	normCentral = {}
	for k,v in eigenCenter.items():
		norm_val = v/center_sum
		normCentral[k] = norm_val
	lottery_node = np.random.choice(normCentral.keys(), p=normCentral.values())
	return lottery_node




if __name__ == "__main__":
	edgeList = readEdgeList('edgeList.csv')
	#list1 = edgeList[:50]
	#list2 = edgeList[50:]
	#degree(edgeList, "out")
	#combined = combineEdgeLists(list1, list2)
	diGraph = pandasToNetworkX(edgeList)
	print randomCentralNode(diGraph)
	