import pandas as pd 
import networkx as nx 
import numpy as np 
import matplotlib.pyplot as plt 

def readEdgeList(filename):
	edge = pd.read_csv(filename)
	shape = edge.shape
	if shape[1] != 2:
		print "Error: contains more than 2 columns"
		return edge[:1]
	return edge

def degree(edgeList, in_or_out):
	if in_or_out == 'in':
		degree = edgeList['1'].value_counts()
	elif in_or_out == 'out':
		degree = edgeList['0'].value_counts()
	return degree
	
def combineEdgeLists(edgeList1, edgeList2):
	lists = [edgeList1, edgeList2]
	edgeList = pd.concat(lists)
	edgeList = edgeList.drop_duplicates()
	return edgeList
	
def pandasToNetworkX(edgeList):
	DG = nx.DiGraph()
	for x, y in edgeList.to_records(index=False):
		DG.add_edge(x,y)
	return DG
	
def randomCentralNode(inputDiGraph):
	centrality_dict = nx.eigenvector_centrality(inputDiGraph)
	normed_dict = {}
	sum = 0
	for key, value in centrality_dict.items():
		sum = value + sum
	for key, value in centrality_dict.items():
		normed_eigen = value/sum
		normed_dict[key] = normed_eigen
	central_node = np.random.choice(normed_dict.keys(), p = normed_dict.values())
	return central_node

