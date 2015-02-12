import unicodecsv as csv
import matplotlib.pyplot as plt

def getBarChartData():
#Open csv files for artists and albums
    f_artists = open('artists.csv')
    f_albums = open('albums.csv')

#Breaks down each csv file by row using reader() method.
    artists_rows = csv.reader(f_artists)
    albums_rows = csv.reader(f_albums)

#First row (literally the "next" row) is the header.
    artists_header = artists_rows.next()
    albums_header = albums_rows.next()

#Create empty list.
    artist_names = []

#Create a list from 1900 to 2020, counting by 10. Create an empty dictionary.    
    decades = range(1900,2020, 10)
    decade_dict = {}
	#Make each entry in decades a key in the empty dictionary. Put 0 in as a placeholder for value.
    for decade in decades:
        decade_dict[decade] = 0
    
#Iterates over every item in artists_rows, and therefore every row in the csv. Assigns each column of the row (1 value) to a variable. Appends artist name to artist_names list.
    for artist_row in artists_rows:
    	if not artist_row:
            continue
        artist_id,name,followers, popularity = artist_row
        artist_names.append(name)

#Iterates over every item in albums_rows, and therefore every row in the csv. Assigns each column of the row (1 value) to a variable.
    for album_row  in albums_rows:
        if not album_row:
            continue
        print album_row
        artist_id, album_id, album_name, year, popularity = album_row
        #Find the decade range wherein the album was released. Increase the count on the decade_dict to reflect the number of albums released in that decade. 
        for decade in decades:
            if (int(year) >= int(decade)) and (int(year) < (int(decade) + 10)):
                decade_dict[decade] += 1
                #Break out of the for loop once the decade is found.
                break
	
	#set x_values to generated list of decades. Set y-values to the values of the decade_dict dictionary (count of albums per decade).
    x_values = decades
    y_values = [decade_dict[d] for d in decades]
    return x_values, y_values, artist_names

def plotBarChart():
	#Call above method to generate these lists.
    x_vals, y_vals, artist_names = getBarChartData()
    
    #Create a figure and pair of axes. Plot the lists we want as x,y data.
    fig , ax = plt.subplots(1,1)
    ax.bar(x_vals, y_vals, width=10)
    
    #Set x, y axis labels and title. Show figure.
    ax.set_xlabel('decades')
    ax.set_ylabel('number of albums')
    ax.set_title('Totals for ' + ', '.join(artist_names))
    plt.show()

if __name__ == "__main__":
	getBarChartData()