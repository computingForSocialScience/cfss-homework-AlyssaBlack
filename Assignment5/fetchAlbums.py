import requests
from datetime import datetime

def fetchAlbumIds(artist_id):
    """Using the Spotify API, take an artist ID and 
    returns a list of album IDs in a list
    """
    url = "https://api.spotify.com/v1/artists/" +artist_id+ '/albums?market=US&album_type=album'
    r = requests.get(url).json()
    items = r['items']
    id = []
    for i in range(len(items)):
    	id.append(items[i]['id'])
    #print id
    return id
    
#fetchAlbumIds('6UE7nl9mha6s8z0wFQFIZ2')


def fetchAlbumInfo(album_id):
    """Using the Spotify API, take an album ID 
    and return a dictionary with keys 'artist_id', 'album_id' 'name', 'year', popularity'
    """
    url = "https://api.spotify.com/v1/albums/" +album_id
    r = requests.get(url).json()
    #print url
    albuminfo = {}
    
    artist = r['artists'][0]
    id = artist['id']
    #print id
    albuminfo['artist_id'] = id
    
    album_id = r['id']
    albuminfo['album_id'] = album_id
    
    name = r['name']
    albuminfo['name'] = name
    
    year = r['release_date'][0:4]
    albuminfo['year'] = year
    
    popularity = r['popularity']
    albuminfo['popularity'] = popularity
    #print albuminfo
    return albuminfo
    

#fetchAlbumInfo('4ektWErsV6EIxW0jBWq1Jn')