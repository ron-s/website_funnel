import csv
from datetime import datetime
import json



read tab-delimited file
def reader():
	with open('tab_delim.tsv', 'r') as filein:
		reader = csv.reader(filein, delimiter='\t')
		yield from reader #generator for low memory usage



def transform_date(date_str):
	# do operation
	date_str = '1/1/2012 5:21:30 AM'
	datetime_object = datetime.strptime("date_str", "%m/%d/%Y %I/%M/%S/")

	return datetime_object



for contents in reader():
	date, name, url = contents
	date = transform_date(date)




	pass





# # write comma-delimited file (comma is the default delimiter)
# with open('comma_delim.csv', 'w') as fileout:
# 	writer = csv.writer(fileout)
# 	for contents in reader():
# 		writer.writerow(contents)
