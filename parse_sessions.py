#import csv
from datetime import datetime
import pdb



#convert weblog datetime to unix datetime
#existing datetime string  '1/1/2012 5:21:30 AM'
def transform_date(date_str):
    """convert weblog datetime to unix datetime"""

    #date_str = '1/1/2012 5:21:30 AM'
    datetime_object = datetime.strptime(date_str, "%m/%d/%Y %I:%M:%S %p")

    return datetime_object




rows = []

with open("./filein.txt", 'r') as filein:
    for line in filein:
        #print(line)
        #remove the new line character
        line = line[:-1]
        #separate the tabbed values in the row
        date, user, url = line.split("\t")

        rows.append({'date': date, 'user': user, 'url': url})

#create a new list to append all sessions
sorted_rows = []


while True:

    if len(rows) > 0:
        row = rows.pop()
        #print(row)

        #remove the item parsed from the rows list after being iterated
        for session in sorted_rows:
            #if a session for the user already exists then append URL and Date to the pages list for that session
            if row['user'] == session['user']:
                session['pages'].append({'date': row['date'], 'url': row['url']})
                break
        else:
            #create a new session with user's information
            sorted_rows.append( {'user': row['user'], 'pages': [{'date': row['date'], 'url': row['url']}]})

    else:
        break


#parse all sessions for each user by date to determine the time delta between the user's visits
#for key,value in sessions.items():



sessions = []


counter = 1
for user_data in sorted_rows:
        if counter <= len(sorted_rows):
            
            visits = user_data['pages']

            for visit in visits:

                    import pdb; pdb.set_trace()
                    start = visit[counter - 1]['date']
                    end = visit[counter]['date']
                    delta = end - start

                    #1200s in 20minutes
                    if delta.seconds >= 1200:
                        sessions.append(user_visit)

                    counter += 1    

            #determine whether time delta is greater than 20min.
            #if greater than 20min then create a new session

print(sessions)




