from io import open
from fetchArtist import *
from fetchAlbums import *

def writeArtistsTable(artist_info_list):
    """Given a list of dictionries, each as returned from 
    fetchArtistInfo(), write a csv file 'artists.csv'.

    The csv file should have a header line that looks like this:
    ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY
    """
    f = open('artists.csv','w')
    f.write(u'ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY\n')

    
    for i in range(len(artist_info_list)):
    	print i
    	print artist_info_list[i]
    	f.write(artist_info_list[i]['id'])
    	f.write(u',')
    	f.write("%s" %artist_info_list[i]["name"])
    	f.write(u',')
    	f.write(unicode(artist_info_list[i]['followers']))
    	f.write(u',')
    	f.write(unicode(artist_info_list[i]['popularity']))
    	f.write(u'\n')
    f.close()


def writeAlbumsTable(album_info_list):
    """
    Given list of dictionaries, each as returned
    from the function fetchAlbumInfo(), write a csv file
    'albums.csv'.

    The csv file should have a header line that looks like this:
    ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY
    """
    f = open('albums.csv','w')
    f.write(u'ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY\n')
    
    for i in range(len(album_info_list)):
    	f.write(album_info_list[i]['artist_id'])
    	f.write(u',')
    	f.write(album_info_list[i]['album_id'])
    	f.write(u',')
    	f.write("%s" %album_info_list[i]['name'])
    	f.write(u',')
    	f.write(unicode(album_info_list[i]['year']))
    	f.write(u',')
    	f.write(unicode(album_info_list[i]['popularity']))
    	f.write(u'\n')
    f.close()
    
if __name__ == "__main__":
	artist_list = ["Fleetwood Mac", "Death Cab for Cutie"]
	artist_info_list = []
	artist_album_list = []
	album_list = []
	album_info_list = []
	
	for i in range(len(artist_list)):
		artist_info_list.append(fetchArtistInfo(fetchArtistId(artist_list[i])))
		artist_album_list = (fetchAlbumIds(fetchArtistId(artist_list[i])))
		for j in range(len(artist_album_list)):
			album_list.append(artist_album_list[j])
	
	for k in range(len(album_list)):
		album_info_list.append(fetchAlbumInfo(album_list[k]))
	
	writeAlbumsTable(album_info_list)
	writeArtistsTable(artist_info_list)