from requests import *
#import sys
import pandas as pd 
import numpy as np
import csv 
#import matplotlib

pd.set_option('display.mpl_style', 'default')

def getRelatedArtists(artistID):
	link = "https://api.spotify.com/v1/artists/%s/related-artists" %artistID
	page = get(link).json()
	page = page['artists']

	rel_artists = []
	rel_ids = []

	for i in range(len(page)):
		rel_artists.append(page[i]['name'])
		rel_ids.append(page[i]['id'])

	#print rel_artists
	#print rel_ids
	return rel_ids

def getDepthEdges(artistID, depth): 
	extended_family = []

	deep = 0
	search = [artistID]
	#while we still have not gone deep enough
	while deep < depth:
		#for each element of the list of artists we are diving into
		for i in range(len(search)):
			#set cousins as the musical first cousins of artist i
			cousins = getRelatedArtists(search[i])
			next_gen = []
			#for each cousin define an edge and add to musical extended_family list if not already included
			for j in range(len(cousins)):
				edge = (search[i], cousins[j])
				is_in = False
				#check if the edge is already written
				for link in range(len(extended_family)):
					if extended_family[link] == edge:
						is_in = True
				#if not already in, include in list and add artist to next generation list to search
				if is_in == False:
					extended_family.append(edge)
					next_gen.append(cousins[j])
		#set the search for the next depth level as the list of artists from this level
		search = next_gen
		deep = deep + 1
	#print extended_family
	return extended_family

def getEdgeList(artistID, depth):
	art_family = getDepthEdges(artistID, depth)
	family_table = pd.DataFrame(art_family)
	#print family_table[:10]
	return family_table

def writeEdgeList(artistID, depth, filename):
	writeTo = open(filename, 'w')
	writeTo.write(getEdgeList(artistID, depth).to_csv(index=False))


if __name__ == "__main__":
	#getRelatedArtists('4gzpq5DPGxSnKTe4SA8HAU')
	#getEdgeList('4gzpq5DPGxSnKTe4SA8HAU',2)
	#getRelatedArtists(sys.argv[1])
	#print getDepthEdges(4gzpq5DPGxSnKTe4SA8HAU', 2)
	writeEdgeList('4gzpq5DPGxSnKTe4SA8HAU', 2, "edgeList.csv")
