from pymongo import MongoClient
import datetime as dt
import time
import random

print('starting...')

client=MongoClient('localhost', 27017)
db = client.test
coll = db.Sensors
print(db)

for x in range(0, 1000):
    ff = random.randrange(60, 90) + random.random()
    ff = round(ff, 2)
    post1 = {
        'node_id': '50',
        "time": dt.datetime.utcnow().timestamp(),
        'type': 'F',
        'value': "b'" + str(ff) + "'v"
    }
    coll.insert_one(post1)

    ff = random.randrange(60, 90) + random.random()
    ff = round(ff, 2)
    post2 = {
        'node_id': '47',
        "time": dt.datetime.utcnow().timestamp(),
        'type': 'F',
        'value': "b'" + str(ff) + "'v"
    }
    coll.insert_one(post2)

    ff = random.randrange(60, 90) + random.random()
    ff = round(ff, 2)
    post3 = {
        'node_id': '50',
        "time": dt.datetime.utcnow().timestamp(),
        'type': 'H',
        'value': "b'" + str(ff) + "'v"
    }
    coll.insert_one(post3)

    print('inserted')
    time.sleep(1)

