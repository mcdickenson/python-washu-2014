from pymongo import Connection
from collections import Counter 
import time 

# Create connection to MongoDB Server
server = 'your_server'
port = 37627
db_name = 'your_db'
username = 'your_username'
password = 'your_password'

connection = Connection(server, port)
db = connection[db_name]
db.authenticate(username, password)
events = db.events

# queries
events.count() # 610 

# 1. Query by candidate: who had most events? who had least?
candidates = []
for c in events.find({'candidate': {'$gt': "A"}}):
	candidates.append(c['candidate'])
candidate_event_count = Counter(candidates)

# 2. Query by state: which had most? which had least?

# 3. Query by city: which had most events?

# 4. What was the most frequently occurring event type in the most popular city?

# 5. What other cities are $within the box bounded by [40.8, -96.7] and [43.6, -91.6]?
# how many events there?
# what was the most frequent type of event?

# 6. what other cities are within a 100 mile radius around 2nd most popular city?
# hint: the earth's radius is about 3963.192 miles
# how many events there? 

# 7. how many kilometers did the candidate with least events travel?
# (assume only stops on this itinerary)
# what was the avg distance travelled per day? 

connection.disconnect()