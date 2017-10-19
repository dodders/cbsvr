from flask import Flask
from flask import request
from pymongo import MongoClient
import json


client = MongoClient('localhost', 27017)  # make this explicit
db = client['test']
coll = db['people']
app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    r = request
    print(r)
    return 'hello ' + request.args.get('name', '')


@app.route("/people/<person_id>", methods=['GET'])
def people(person_id):
    print("retrieving for %s..." % person_id)
    docs = []
    cursor = coll.find({'key': person_id})
    for doc in cursor:
        # serialization support
        doc['_id'] = str(doc['_id'])
        docs.append(doc)
    # return number of documents and document list.
    docs.insert(0, docs.__len__())
    return json.dumps(docs)
    # return "ok!"


app.run()

