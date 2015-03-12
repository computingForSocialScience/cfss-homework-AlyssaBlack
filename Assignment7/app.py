from flask import Flask, render_template, request, redirect, url_for
import pymysql
 
from artistNetworks import *
from analyzeNetworks import *
from fetchArtist import *
from fetchAlbums import *
from makePlaylist import *

dbname="playlists"
host="localhost"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')
c = db.cursor()

app = Flask(__name__)

def createNewPlaylist(artist):
	sql = "CREATE TABLE IF NOT EXISTS playlists (id INT PRIMARY KEY AUTO_INCREMENT, rootArtist VARCHAR(500)) ENGINE=MyISAM DEFAULT CHARSET=utf8"
	sql2 = "CREATE TABLE IF NOT EXISTS songs (playlistId INT, songOrder INT(8), artistName VARCHAR(500), albumName VARCHAR(500), trackName VARCHAR(500)) ENGINE=MyISAM DEFAULT CHARSET=utf8"
	c.execute(sql)
	c.execute(sql2)
	
	insert_artist = "INSERT INTO playlists (rootArtist) VALUES ('%s')" %artist
	c.execute(insert_artist)
	artist_id = "SELECT id FROM playlists WHERE rootArtist = '%s'" %artist
	c.execute(artist_id)
	rootId = c.fetchall()[0][0]
	print "rootId", type(rootId)
	
	#artists = fetchNetwork([artist])
	#print "artists" artists
	#song_playlist = playlist(artists)
	#print "song_playlist" song_playlist[0]
	#song_playlist = writePlayList(artist, file)
	print "about to enter loop"
	artists = chooseArtists([artist])
	song_playlist = chooseList(artists)
	order = 1
	for i in song_playlist:
		print "i is:", i
		artist_name = str(i[0])
		print type(artist_name)
		album_name = str(i[1])
		track_name = str(i[2])
		add_song = 'INSERT INTO songs (playlistId, songOrder, artistName, albumName, trackName) VALUES (%d, %d, %s, %s, %s)' %(rootId, order, artist_name, album_name, track_name)
		c.execute(add_song)
		order = order + 1
	db.commit()
	c.close()
	db.close()
	
@app.route('/')
def make_index_resp():
    # this function just renders templates/index.html when
    # someone goes to http://127.0.0.1:5000/
    #createNewPlaylist('Robyn')
    return(render_template('index.html'))


@app.route('/playlists/')
def make_playlists_resp():
	c.execute('SELECT * FROM playlists')
	playlists = c.fetchall()
	return render_template('playlists.html',playlists=playlists)


@app.route('/playlist/<playlistId>')
def make_playlist_resp(playlistId):
    return render_template('playlist.html',songs=songs)


@app.route('/addPlaylist/',methods=['GET','POST'])
def add_playlist():
    if request.method == 'GET':
        # This code executes when someone visits the page.
        return(render_template('addPlaylist.html'))
    elif request.method == 'POST':
        # this code executes when someone fills out the form
        artistName = request.form['artistName']
        # YOUR CODE HERE
        return(redirect("/playlists/"))



if __name__ == '__main__':
    #app.debug=True
    #createNewPlaylist("Spoon")
    #createNewPlaylist("Coldplay")
    app.run()
    