import sys
import random
from io import open
from artistNetworks import *
from analyzeNetworks import *
from fetchArtist import *
from fetchAlbums import *

def chooseArtists(inputs):
	#get ids of all inputted artists
	artistIDs = []
	for artist in inputs:
		artistIDs.append(fetchArtistId(artist))
	#get concatenate lists of family trees
	for artist in artistIDs:
		art_edge = getEdgeList(artist, 2)
		is_in = False
		if 'edge_list' in locals():
			edge_list = combineEdgeLists(art_edge, edge_list)
		else:
			edge_list = art_edge		
	#make graph
	edgeGraph = pandasToNetworkX(edge_list)
	#choose 30 random artists
	play_artists = []
	for i in range(30):
		play_artists.append(randomCentralNode(edgeGraph))

	return play_artists

def chooseAlbums(artists):
	play_albums = []
	for i in range(len(artists)):
		art_albums = fetchAlbumIds(artists[i]) 
		if len(art_albums) > 0:
			play_albums.append(random.choice(art_albums))
	return play_albums

def fetchSongs(album):
	songs_link = 'https://api.spotify.com/v1/albums/%s/tracks' %album
	songs_page = get(songs_link).json()
	songs_list = songs_page['items']

	songs = []
	
	for i in range(len(songs_list)):
		songName = "%s" %songs_list[i][u'name']
		artistName = "%s" %songs_list[i][u'artists'][0][u'name']
		songs.append((songName, artistName))

	return songs

def chooseList(artists):
	albums = chooseAlbums(artists)
	play_list = []
	for i in range(len(albums)):
		album_songs = fetchSongs(albums[i])
		if len(album_songs) > 0:
			choice = random.choice(album_songs)
			artistName = '"%s"' %choice[1]
			songName = '"%s"' %choice[0]
			albumName = '"%s"' %fetchAlbumInfo(albums[i])['name']
			choice = (artistName, albumName, songName)
			play_list.append(choice)
	#print "play list starts with:", play_list[:5]

	return play_list

def writePlayList(inputs, filename):
	artists = chooseArtists(inputs)
	play_list = chooseList(artists)
	playList = open (filename, 'w', encoding = 'utf-8')

	playList.write(u'Artist Name, Album Name, Track Name')
	#playList.write(u'\n')

	for entry in play_list:
		playList.write(u'\n')
		playList.write(entry[0])
		playList.write(u',')
		playList.write(entry[1])
		playList.write(u',')
		playList.write(entry[2])
    	#playList.write(u'\n')


if __name__ == "__main__":
	inputs = sys.argv[1:]
	#artists = chooseArtists(inputs)
	#songs = chooseList(artists)
	writePlayList(inputs, "playList.csv")
