import csv
from datetime import datetime
from operator import itemgetter
import json
from collections import namedtuple



def reader(filename):
    #read tab-delimited file
    with open(filename, 'r') as filein:
        reader = csv.reader(filein, delimiter='\t')
        #generator for low memory usage
        yield from reader


def write():
    #write json file
    with open('file.json', 'w') as fileout:
        writer = json.writer(fileout, indent=4)
        fileout = json.dumps([row for row in reader])
        jsonfile.write(fileout)


def transform_date(date_str):
    # do operation
    #date_str = '1/1/2012 5:21:30 AM'
    datetime_object = datetime.strptime(date_str, "%m/%d/%Y %I:%M:%S %p")

    return datetime_object


def build_user_data(filename):
    #define the content in the tabbed delimited rows,
    #and gather all associated data for each user into a dictionary
    accumulator = []
    #instatiating a named tuple
    tuplename = namedtuple("username", ["user", "date", "url"])

    for row in reader(filename):
        date, user, url = row
        date = transform_date(date)
        

        accumulator.append(tuplename(user,date,url))





    return accumulator


def sort(accumulator):
    #sort the rows in the accumulator by date

    #sort_by_date = sorted(accumulator, key=lambda date: date)


    sort_by_user = sorted(accumulator, key=itemgetter(0))
    print(sort_by_user)





# # write comma-delimited file (comma is the default delimiter)
# with open('comma_delim.csv', 'w') as fileout:
#     writer = csv.writer(fileout)
#     for contents in reader():
#         writer.writerow(contents)
