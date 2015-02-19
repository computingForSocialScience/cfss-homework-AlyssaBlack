import sys
import random
from io import open
from artistNetworks import *
from analyzeNetworks import *
from fetchArtist import *
from fetchAlbums import *

def fetchSongs(album):
	songs = []
	url = 'https://api.spotify.com/v1/albums/' +album+ '/tracks'
	r = get(url).json()
	song_list = r['items']
	
	for i in range(len(song_list)):
		songName = '"%s"' %song_list[i][u'name']
		artist = '"%s"' %song_list[i][u'artists'][0][u'name']
		songs.append((songName, artist))
	return songs
	
def fetchNetwork(artists):
	IDs = []
	for i in artists:
		IDs.append(fetchArtistId(i))
	for j in IDs:
		artist_edges = getEdgeList(j,2)
		present = False
		if 'edge_list' in locals():
			edge_list = combineEdgeLists(artist_edges, edge_list)
		else:
			edge_list = artist_edges
	g = pandasToNetworkX(edge_list)
		
	network = []
	for k in range(30):
		network.append(randomCentralNode(g))
	return network


def getAlbums(artists):
	albums = []
	for i in range(len(artists)):
		artist_albums = fetchAlbumIds(artists[i])
		if len(artist_albums) > 0:
			albums.append(random.choice(artist_albums))
	return albums

def playlist(artists):
	playlist = []
	albums = getAlbums(artists)
	for i in range(len(albums)):
		songs = fetchSongs(albums[i])
		if len(songs) > 0:
			pick = random.choice(songs)
			song = '"%s"' %pick[0]
			artist = '"%s"' %pick[1]
			album = '"%s"' %fetchAlbumInfo(albums[i])['name']
			playlist_song = (artist, album, song)
			playlist.append(playlist_song)
	return playlist

def writePlayList(artist, file):
	artists = fetchNetwork(artist)
	play_list = playlist(artists)
	
	f = open(file, 'w',encoding = 'utf-8')
	f.write(u'artist_name, album_name, track_name')
	for i in play_list:
		f.write(u'\n')
		f.write(i[0])
		f.write(u',')
		f.write(i[1])
		f.write(u',')
		f.write(i[2])

if __name__ == "__main__":
	inputs = sys.argv[1:]
	writePlayList(inputs, "playlist.csv")

