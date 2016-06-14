import csv
from datetime import datetime


# read tab-delimited file
with open('tab_delim.tsv', 'rb') as filein:
    reader = csv.reader(filein, delimiter='\t')
    filecontents = [line for line in read]

# write comma-delimited file (comma is the default delimiter)
with open('comma_delim.csv', 'wb') as fileout:
    writer = csv.writer(fileout, quotechar='')
    writer.writerows(filecontents)
