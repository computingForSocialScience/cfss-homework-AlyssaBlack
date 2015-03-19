import sys
import requests
import pymysql
from flask import Flask, render_template, request, redirect, url_for
#it's called census3.py on my computer
from census3 import *
import numpy as np
import pandas as pd

dbname="census"
host="localhost"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')

webpage = Flask(__name__)
IDs = ['B19019']
@webpage.route('/')
def make_index_resp():
    # this function just renders templates/index.html when
    # someone goes to http://127.0.0.1:5000/
    all_cols = []
    for i in IDs:
    	tableInfo, colIdOrder = getTableInfo(i)
    	all_cols.append(colIdOrder)
    print all_cols
    print tableInfo
    return render_template('index.html', all_cols = all_cols)

@webpage.route('/compare?state=[FIPSCode]&col1=[columnId1]&col2=[columnId2]')
def basic_comparison(FIPSCode, columnId1, columnId2):
	c = db.cursor()
	#get tableID from selected columns
	table1 = "SELECT tableID FROM columnInfoTable WHERE colID = 'columnId1'"
	table2 = "SELECT tableID FROM columnInfoTable WHERE colID = 'columnId2'"
	c.execute(table1)
	table1 = str(c.fetchall())
	c.execute(table2)
	table2 = str(c.fetchall())
	
	#get id of denominator columns
	denominator1_id = "SELECT denomColId FROM" +table1+ "WHERE colID = 'columnId1'"
	denominator2_id = "SELECT denomColId FROM" +table2+ "WHERE colID = 'columndId2'"
	c.execute(denominator1_id)
	denominator1_id = c.fetchall()
	c.execute(denominator2_id)
	denominator2_id = c.fetchall()
	
	#get denominator values
	denominator1 = "SELECT * FROM" +table1+ "WHERE colID = 'denominator1_id'"
	denominator2 = "SELECT * FROM" +table2+ "WHERE colID = 'denominator2_id'"
	c.execute(denominator1)
	denominator1 = c.fetchall()
	c.execute(denominator2)
	denominator2 = c.fetchall()
	
	#get data from chosen columns
	select = "SELECT columnId1, columnId2 FROM "+table1+"," +table2+" WHERE "+table1+".X="+table2+".X, fips='FIPSCode'"
	c.execute(select)
	data = c.fetchall()
	print data
	
	#compare the data, need to do something with denominator here
	#need to make dict of comparisons?
	data.describe() # the .describe() method in provides a 5 number summary for a pandas series. No idea if it will work on a sql table.
	db.commit()
	c.close()
	return render_template('comparison.html', comparisons = comparisons)

if __name__ == "__main__":
	webpage.debug=True
	webpage.run(port=5001)
	