from pymongo import MongoClient
import datetime as dt
import time

print('starting...')

client=MongoClient('localhost', 27017)
db = client.test
coll = db.people
print(db)

for x in range(0, 1000):

    post1 = {
        "key": "gd",
        "name": "george",
        "location": "gloucester",
        "time": dt.datetime.utcnow().timestamp()
    }
    coll.insert_one(post1).inserted_id
    post2 = {
        "key": "ed",
        "name": "edward",
        "location": "gloucester",
        "time": dt.datetime.utcnow().timestamp()
    }
    coll.insert_one(post2).inserted_id
    print('inserted')
    time.sleep(1)

