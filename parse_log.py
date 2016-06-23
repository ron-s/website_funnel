import csv
from datetime import datetime
from datetime import timedelta


def reader(filename):
    # read tab-delimited file
    with open(filename, 'r') as filein:
        reader = csv.reader(filein, delimiter='\t')
        # generator for low memory usage
        yield from reader


def transform_date(date_str):
    # do operation
    # date_str = '1/1/2012 5:21:30 AM'
    datetime_object = datetime.strptime(date_str, "%m/%d/%Y %I:%M:%S %p")

    return datetime_object


class User:
    def __init__(self, username, date, url):
        self.username = username
        self.url = url
        self.date = date

    def __repr__(self):
        return self.username


def build_user_data(filename):
    accumulator = []
    for row in reader(filename):
        date, user, url = row
        date = transform_date(date)
        ins = User(user, date, url)
        accumulator.append(ins)
    return accumulator


def sort(accumulator):
    newdict = {}
    accumulator.sort(key=lambda n: n.username, reverse=True)
    for x in accumulator:
        if x.username in newdict:
            newdict[x.username].append(x)
        else:
            newdict[x.username] = [x]
    return newdict


def get_sessions(dictionary_of_users):
    sessions = {}
    for key, value in dictionary_of_users.items():
        x = 0
        # print()
        temp = set()
        for i in range(0, len(value)-1):
            # print(value[i].username)
            time = abs(value[i].date - value[i+1].date)
            if time <= timedelta(0, 0, 0, 0, 20):
                temp.add(value[i])
                temp.add(value[i+1])
        else:
            sessions[key] = sorted(temp, key=lambda n: n.date, reverse=False)
    return sessions


def get_best_funnel(sessions):
    session_funnel_filter = []
    session_dict = {}
    for k, v in sessions.items():
        session_funnel = []
        for obj in v:
            session_funnel.append(obj.url)
        if len(session_funnel) > 0:
            session_funnel_filter.append(session_funnel)
    for ses in session_funnel_filter:
        funnel = ''.join(ses)
        if funnel not in session_dict:
            session_dict[funnel] = 1
        else:
            session_dict[funnel] += 1
    most_seen = max(session_dict, key=session_dict.get)
    print('The most common session seems to be {} at {} occurrences.'.format(most_seen, session_dict[most_seen]))


get_best_funnel(get_sessions(sort(build_user_data('filein.txt'))))