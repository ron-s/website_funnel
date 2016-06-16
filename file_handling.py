import csv
from datetime import datetime
import json



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
    #define content in the rows and gather all associated data for each user into a list of dictionaries
    accumulator = []

    for row in reader(filename):
        date, user, url = row
        date = transform_date(date)

        userdata = {"user": user, "date": date, "url": url}
        accumulator.append(userdata)

    return accumulator






# # write comma-delimited file (comma is the default delimiter)
# with open('comma_delim.csv', 'w') as fileout:
#     writer = csv.writer(fileout)
#     for contents in reader():
#         writer.writerow(contents)
