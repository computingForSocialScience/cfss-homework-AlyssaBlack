import sys
import requests
import pymysql
from flask import Flask, render_template, request, redirect, url_for
#it's called census3.py on my computer
from censusFinal import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import tempfile


dbname="census"
host="localhost"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')

webpage = Flask(__name__)
IDs = ['B19019']
@webpage.route('/')
def make_index_resp():
    """# this function just renders templates/index.html when
    # someone goes to http://127.0.0.1:5000/
    all_cols = []
    for i in IDs:
    	tableInfo, colIdOrder = getTableInfo(i)
    	all_cols.append(colIdOrder)
    	print all_cols
    print all_cols
    return render_template('index.html', all_cols = all_cols)
    """
    c = db.cursor()
    c.execute("SELECT colID, colName FROM columnInfoTable")
    tables = c.fetchall() 
    #print tables
    return render_template('index.html', all_cols = tables)


#@webpage.route('/compare?state=[FIPSCode]&col1=[columnId1]&col2=[columnId2]')
@webpage.route('/compare/')
def basic_comparison():
	#FIPSCode, columnId1, columnId2 = 
	FIPSCode = request.args.get('state')
	columnId1 = request.args.get('col1')
	columnId2 = request.args.get('col2')
	columnId1 = str(columnId1)
	columnId2 = str(columnId2)
	
	c = db.cursor()
	#get tableID from selected columns
	table1 = """SELECT tableID FROM columnInfoTable WHERE colID = '%s'""" % str(columnId1)
	table2 = """SELECT tableID FROM columnInfoTable WHERE colID = '%s'""" % str(columnId2)

	c.execute(table1)
	table1_id = str(c.fetchall()[0][0])
	c.execute(table2)
	table2_id = str(c.fetchall()[0][0])
	#print type(columnId1)
	print table2_id
	
	
	#get id of denominator columns from info table
	denominator1_id = """SELECT denomColId FROM columnInfoTable WHERE colID = '%s'""" % columnId1
	c.execute(denominator1_id)
	denominator1_id = str(c.fetchall()[0][0])
	
	denominator2_id = """SELECT denomColId FROM columnInfoTable WHERE colID = '%s'""" % columnId2
	c.execute(denominator2_id)
	denominator2_id = str(c.fetchall()[0][0])
	#print denominator1_id, type(denominator1_id)
	#print denominator2_id, type(denominator2_id)
	
	#####
	if denominator1_id != "None":
	#get denominator values- currently a tuple of tuples of lists
		denominator1 = "SELECT "+denominator1_id+" FROM "+table1_id+" WHERE fips = '%s'" % str(FIPSCode)
		c.execute(denominator1)
		denominator1 = c.fetchall()
	
	if denominator2_id != "None":
		denominator2 = "SELECT " +denominator2_id+ " FROM "+table2_id+" WHERE fips = '%s'" % str(FIPSCode)
		c.execute(denominator2)
		denominator2 = c.fetchall()
	#print denominator1, type(denominator1)
	#print denominator2, type(denominator2)
	#######
	
	#get data from chosen columns
	#print type(FIPSCode)
	if table1_id != table2_id:
		select = "SELECT "+columnId1+", "+columnId2+" FROM "+table1_id+", " +table2_id+" WHERE "+table1_id+".geoID="+table2_id+".geoID AND "+table1_id+".fips = '%s' AND "% str(FIPSCode) +table2_id+".fips = '%s'" % str(FIPSCode)
		#print select
		c.execute(select)
		data = c.fetchall()
		print data
		#print type(data)
	#######	
	else:
		select = "SELECT "+columnId1+", "+columnId2+" FROM "+table1_id+" WHERE fips = '%s'" % str(FIPSCode)
		c.execute(select)
		data = c.fetchall()
		
	########
	#compare the data, need to do something with denominator here
	#need to make dict of comparisons?
	if type(data) != None:
		x = []
		y = []
		for item in data:
			print item
			x.append(float(item[0]))
			y.append(float(item[1]))
			#print type(item[0])
			#print type(item[0])
		print x
		print y
		plt.clf()
		ax = plt.axes()
		ax.scatter(x,y)
		name1 = "SELECT colName FROM columnInfoTable WHERE colID = '%s'" % str(columnId1)
		c.execute(name1)
		name1 = c.fetchall()[0][0]
		name1 = str(name1)
		
		name2 = "SELECT colName FROM columnInfoTable WHERE colID = '%s'" % str(columnId2)
		c.execute(name2)
		name2 = c.fetchall()[0][0]
		name2 = str(name2)
		ax.set_title("%s by %s" % (str(name2), str(name1)))

		ax.set_xlabel('%s' % (str(columnId1)))
		ax.set_ylabel('%s' % (str(columnId2)))
		plt.draw
		#plt.show()
		f = tempfile.NamedTemporaryFile(dir='static/temp/', suffix='.png', delete=False)
		plt.savefig(f)
		f.close()
		plotPng = f.name.split('/')[-1]
		
		#plt.savefig("/Users/ABlackburn/cfss/cfss-homework-AlyssaBlack/final_project/templates/plot.png")
		info = []
		slope, intercept, r, p, stderr = linregress(x, y)
		info.append(str(slope))
		info.append(str(intercept))
		info.append(str(r))
		info.append(str(p))
		info.append(str(stderr))
		print info
		print type(info)
		
	db.commit()
	c.close()
	return render_template('comparison.html', comparisons=data, plotPng=plotPng, info=info, slope=slope, intercept=intercept, r=r, p=p, stderr=stderr)

if __name__ == "__main__":
	webpage.debug=True
	webpage.run(port=5005)
	