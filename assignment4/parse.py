import csv
import sys
import matplotlib.pyplot as plt
#hello
def readCSV(filename):
    '''Reads the CSV file `filename` and returns a list
    with as many items as the CSV has rows. Each list item 
    is a tuple containing the columns in that row as stings.
    Note that if the CSV has a header, it will be the first
    item in the list.'''
    with open(filename,'r') as f:
        rdr = csv.reader(f)
        lines = list(rdr)
    return(lines)

#file = readCSV('permits.csv')
#print len(file)
#print len(file[0])
#item = file[1]
#print item[128], item[129]
### enter your code below

def get_avg_latlng(filename):
	file = readCSV(filename)
	lat=0.0
	lng=0.0
	total=0.0
	i=1
	while i < len(file):
		item = file[i]
		if item[128] and item[129] != '':
			lat = float(item[128]) + lat
			lng = float(item[129]) + lng
			total +=1
		i+=1		
	avg_lat = lat/total
	avg_lng = lng/total
	print avg_lat, avg_lng
	
get_avg_latlng('permits.csv')

def zip_code_barchart(filename):
	file = readCSV(filename)
	zipcodes = []
	zipcode_count = []
	zip_dict = {}
	
	i = 1
	while i < len(file):
		print i
		item = file[i]
		j = 28
		while j < 128:
			print j
			if item[j] != '' and item[j] != 'IL':
				new_zip = item[j][0:5]
				new_zip = float(new_zip)
				print new_zip
				zipcodes.append(new_zip)
			j = j + 7
		i+=1
	#print zipcodes	
	plt.hist(zipcodes, bins=200)
	plt.title("Histogram of Contractor Zip Codes in Hyde Park")
	plt.show()

#Hunter's response in Piazza said it was okay to just graph hyde park permits
zip_code_barchart('permits_hydepark.csv')
	
if __name__ == "__main__":
	function = sys.argv[1]
	filename = sys.argv[2]
	if function == "latlong":
		print get_avg_latlng(filename)
	elif function == "hist":
		print zip_code_barchart(filename)
	else:
		print "Invalid, choose a function and file name."