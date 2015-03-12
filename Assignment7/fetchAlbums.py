from requests import *
from datetime import datetime
from fetchArtist import fetchArtistId

def fetchAlbumIds(artist_id):
    """Using the Spotify API, take an artist ID and 
    returns a list of album IDs in a list
    """
    albumLink = "https://api.spotify.com/v1/artists/%s/albums?market=US&album_type=album" % artist_id
    albumPage = get(albumLink).json()
    albumInfo = albumPage["items"]
    
    albumNames = []
    albumIDs = []
    for i in range(len(albumInfo)):
    	albumNames.append(albumInfo[i]["name"])
    	albumIDs.append(albumInfo[i]["id"])

    #print albumNames
    return albumIDs


def fetchAlbumInfo(album_id):
    """Using the Spotify API, take an album ID 
    and return a dictionary with keys 'artist_id', 'album_id' 'name', 'year', popularity'
    """
    albumLink = "https://api.spotify.com/v1/albums/%s" %album_id
    album = get(albumLink).json()

    albumInfo = {}
    albumInfo['artist_id'] = album["artists"][0]["id"]
    albumInfo["album_id"] = album["id"]
    albumInfo["name"] = album["name"]
    albumInfo["year"] = album["release_date"][0:4]
    albumInfo["popularity"] = album['popularity']

    return albumInfo

    
if __name__ == '__main__':
	#artId = fetchArtistId('coldplay')
	print(fetchAlbumIds('16s0YTFcyjP4kgFwt7ktrY'))
	print(len(fetchAlbumIds('16s0YTFcyjP4kgFwt7ktrY')))
	#print(fetchAlbumInfo(fetchAlbumIds(artId)[0]))