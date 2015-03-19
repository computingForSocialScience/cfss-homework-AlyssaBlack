from flask import Flask, render_template, request, redirect, url_for
import pymysql
import sys
import requests
import csv
import re

dbname="Census"
host="localhost"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')

IDs = 'B19125'
def get_table_info(tableID):
	url = 'http://api.censusreporter.org/1.0/table/' +tableID
	r = requests.get(url).json()
	title = r['table_title']
	columns = r['columns']
	column_IDs = []
	column_titles = []
	for k,v in columns.items():
		column_IDs.append(k)
		#print v
		column_titles.append(v[u'column_title'])
	denominator_column_id = r['denominator_column_id']
	#print url
	print title
	#print columns
	print column_IDs
	print column_titles
	print denominator_column_id
	
#get_table_info(IDs)
#get_table_info('B19326')
get_table_info('B19019')
	
def get_table_data(tableID):
	#FIPSurl = 'http://cfss.uchicago.edu/data/FIPS.json'
	FIPS_dict = {"Mississippi": 28, "Oklahoma": 40, "Delaware": 10, "Minnesota": 27, "Illinois": 17, "Arkansas": 5, "New Mexico": 35, "Indiana": 18, "Maryland": 24, "Louisiana": 22, "Idaho": 16, "Wyoming": 56, "Tennessee": 47, "Arizona": 4, "Iowa": 19, "Michigan": 26, "Kansas": 20, "Utah": 49, "Virginia": 51, "Oregon": 41, "Connecticut": 9, "Montana": 30, "California": 6, "Massachusetts": 25, "West Virginia": 54, "South Carolina": 45, "New Hampshire": 33, "Wisconsin": 55, "Vermont": 50, "Georgia": 13, "North Dakota": 38, "Pennsylvania": 42, "Florida": 12, "Alaska": 2, "Kentucky": 21, "Hawaii": 15, "Nebraska": 31, "Missouri": 29, "Ohio": 39, "Alabama": 1, "New York": 36, "South Dakota": 46, "Colorado": 8, "New Jersey": 34, "Washington": 53, "North Carolina": 37, "District of Columbia": 11, "Texas": 48, "Nevada": 32, "Maine": 23, "Rhode Island": 44}
	FIPS_codes = []
	for k,v in FIPS_dict.items():
		FIPS_codes.append(v)
	print FIPS_codes
	for i in FIPS_codes:
		FIPScode = str(i)
		url = 'http://api.censusreporter.org/1.0/data/show/latest?table_ids=<' +tableID+ '>&geo_ids=140|04000US<'+FIPScode+'>'
		print url



#get_table_data(IDs)
#get_table_data('B19326')
#get_table_data('B19013')
get_table_data('B19019')
		
	

	