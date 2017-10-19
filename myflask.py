from flask import Flask
from pymongo import MongoClient
import json


client = MongoClient('localhost', 27017)  # make this explicit
db = client['test']
coll = db['people']
app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world."


@app.route("/people/<id>")
def people(id):
    print("retrieving for %s..." % id)
    docs = []
    cursor = coll.find({'key': id})
    for doc in cursor:
        # serialization support
        doc['_id'] = str(doc['_id'])
        doc['time'] = doc['time'].isoformat()
        docs.append(doc)
    # return number of documents and document list.
    docs.insert(0, docs.__len__())
    return json.dumps(docs)
    # return "ok!"


app.run()

