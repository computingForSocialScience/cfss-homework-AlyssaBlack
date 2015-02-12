import sys
from fetchArtist import fetchArtistId, fetchArtistInfo
from fetchAlbums import fetchAlbumIds, fetchAlbumInfo
from csvUtils import writeArtistsTable, writeAlbumsTable
from barChart import plotBarChart

if __name__ == '__main__':
	artist_names = sys.argv[1:]
	print "input artists are ", artist_names
	# YOUR CODE HERE
	ids = []
	artist_info = []
	album_info = []
	for i in artist_names:
		id = fetchArtistId(i)
		ids.append(id) #list of artist ids
		print ids

	for id in ids:
		artist_info.append(fetchArtistInfo(id)) #creating list of dictionaries of artists' info
		album_ids = fetchAlbumIds(id) #list of album ids for each artist
		print album_ids
		for album_id in album_ids:
			album_info.append(fetchAlbumInfo(album_id)) #list of dictionaries of album info
		print album_info
			
	#create artist csv and album csv
	writeArtistsTable(artist_info)
	writeAlbumsTable(album_info)
	
	plotBarChart()

