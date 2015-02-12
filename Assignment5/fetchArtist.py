import sys
import requests
import csv
import re


def fetchArtistId(name):
    """Using the Spotify API search method, take a string that is the artist's name, 
    and return a Spotify artist ID.
    """
    url = "https://api.spotify.com/v1/search?q=" +name+ "&type=artist"
    r = requests.get(url).json()
    artist = r["artists"]
    #print artist
    items = artist['items']
    pick = items[0]
    id = pick['id']
    #print id
    return id

#fetchArtistId('Robyn')   

def fetchArtistInfo(artist_id):
    """Using the Spotify API, takes a string representing the id and
`   returns a dictionary including the keys 'followers', 'genres', 
    'id', 'name', and 'popularity'.
    """
    url = "https://api.spotify.com/v1/artists/"+artist_id
    r = requests.get(url).json()
    artistinfo = {}
    
    followers = r['followers']
    followers = followers['total']
    artistinfo['followers'] = followers
    
    genres = r['genres']
    artistinfo['genres'] = genres
    
    id = r['id']
    artistinfo['id'] = id
    
    name = r['name']
    artistinfo['name'] = name
    
    popularity = r['popularity']
    artistinfo['popularity'] = popularity
    #print artistinfo
    return artistinfo
    
#fetchArtistInfo('6UE7nl9mha6s8z0wFQFIZ2')
    

