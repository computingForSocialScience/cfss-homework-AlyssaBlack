import sys
import requests
import csv

def fetchArtistId(name):
    """Using the Spotify API search method, take a string that is the artist's name, 
    and return a Spotify artist ID.
    """
    name.replace(" ", "+")
    searchLink = "https://api.spotify.com/v1/search?q=%s&type=artist" %name
    artistPage = requests.get(searchLink)
    artist = artistPage.json()
    artist = artist['artists']
    artistInfo = artist['items']
    artistInfo = artistInfo[0]
    artistID = artistInfo['id']
    #print artistID
    return artistID

def fetchArtistInfo(artist_id):
    """Using the Spotify API, takes a string representing the id and
`   returns a dictionary including the keys 'followers', 'genres', 
    'id', 'name', and 'popularity'.
    """
    searchLink = "https://api.spotify.com/v1/artists/%s" %artist_id
    artist = requests.get(searchLink).json()
    artist['followers'] = artist['followers']['total']
    return artist


if __name__ == '__main__':
    good = fetchArtistId("coldplay")
    print good