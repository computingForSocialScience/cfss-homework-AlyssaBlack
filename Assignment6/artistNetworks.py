from requests import *
import pandas as pd 
import numpy as np
import csv 
import sys

pd.set_option('display.mpl_style', 'default')
def getRelatedArtists(artistID):
	RelatedArtists = []
	url = 'https://api.spotify.com/v1/artists/'+artistID+'/related-artists'
	r = get(url).json()
	artist = r['artists']
	
	for i in range(len(artist)):
		id = artist[i]['id']
		RelatedArtists.append(id)
	return RelatedArtists
	
def getDepthEdges(artistID, depth):
	edges = []
	dig = 0 
	
	search = [artistID]
	#dig to depth
	while dig < depth:
		#each level of search
		for i in range(len(search)):
			related = getRelatedArtists(search[i])
			neighbors = []
			for j in range(len(related)):
				edge = (search[i], related[j])
				present = False
				
				for k in range(len(edges)):
					if edges[k] == edge:
						present = True
				if present == False:
					edges.append(edge)
					neighbors.append(related[j])
		
		search = neighbors
		dig += 1
	return edges
	
def getEdgeList(artistID, depth):
	network_edges = getDepthEdges(artistID, depth)
	data_frame = pd.DataFrame(network_edges)
	return data_frame
	
def writeEdgeList(artistID, depth, filename):
	f = open(filename, 'w')
	f.write(getEdgeList(artistID, depth).to_csv(index=False))
