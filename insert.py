from pymongo import MongoClient
import datetime as dt
import time

print('starting...')

client=MongoClient('localhost', 27017)
db = client.test
coll = db.people
print(db)

for x in range(0, 1000):

    post={
        "key": "gd",
        "name": "george",
        "location": "new york",
        "time": dt.datetime.utcnow()
    }
    id = coll.insert_one(post).inserted_id
    print('inserted', id)
    time.sleep(3)

