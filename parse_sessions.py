import csv
from datetime import datetime




rows = []

with open("./filein.txt", 'r') as filein:
    for line in filein:
        #print(line)
        #remove the new line character
        line = line[:-1]
        #separate the tabbed values in the row
        date, user, url = line.split("\t")

        rows.append({'date': date, 'user': user, 'url': url})

print(rows)

#create a new list to append all sessions
sessions = []

for row in rows
    if 




# class Row:
#     """create a class from the properties of a row in a tab delimited log file"""

#     def __init__(self):
#         user = "user"
#         date = "date"
#         url = "url"


# def reader(filename):
#     """open and read a tabbed delimited file"""
#     #read tab-delimited file
#     with open(filename, 'r') as filein:
#         reader = csv.reader(filein, delimiter='\t')
#         #generator for low memory usage
#         yield from reader



# for i in R:
#     #iterate through the tabbed delimited file to sort the objects by user and add them to a dict
#     if not in data_dict:
#         #if the user doesn't exist in the dict
#         data_dict[i.user] = i

#     else:
#         # if user already exists in the dict
#         data_dict[i.user].append = i


# newlst = set()

# for k, v in data_dict.items():

#     x = 0

#     for i in range(len(v) - 1):
#         time = i[x].date - i[x]+1.date

#         x += 1

#         if time <= datetime.delta(0, 0, 0, 0, 20):
#         #if the difference between the timestamps is 20min or less then it belongs to the same session
#             newlst.add(i[x])
#             newlst.add(i[x + 1])

#         else:
#         #if the difference between the timestamps is greater than 20min then it belongs to a new session
#             break
