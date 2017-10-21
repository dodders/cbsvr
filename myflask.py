from flask import Flask
from flask import request
from pymongo import MongoClient
import json
import datetime as dt


client = MongoClient('localhost', 27017)  # make this explicit
db = client['test']
coll = db['people']
app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    r = request
    print(r)
    dt.date.today()
    return 'hello ' + request.args.get('name', '')


def today():
    now = dt.date.today()
    start = dt.datetime(now.year, now.month, now.day, 0, 0, 0, 0)
    day = dt.timedelta(days=1)
    end = start + day
    return start.timestamp(), end.timestamp()


@app.route("/people/<person_id>", methods=['GET'])
def people(person_id):
    print("retrieving for %s..." % person_id)
    docs = []
    start, end = today()
    qry = {'key': person_id, '$and': [{'time': {'$gte': start}}, {'time': {'$lte': end}}]}
    print('query is %s' % qry)
    cursor = coll.find(qry)
    for doc in cursor:
        # serialization support
        doc['_id'] = str(doc['_id'])
        docs.append(doc)
    # return number of documents and document list.
    docs.insert(0, docs.__len__())
    return json.dumps(docs)
    # return "ok!"


app.run()

