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
        "key": "ed",
        "name": "edward",
        "location": "gloucester",
        "time": dt.datetime.utcnow()
    }
    id = coll.insert_one(post).inserted_id
    print('inserted', id)
    time.sleep(2)

