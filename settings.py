MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_DBNAME = 'test'

PAGINATION = 'false'
#PAGINATION_LIMIT = 500
#PAGINATION_DEFAULT = 100

X_DOMAINS = '*'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
        # read-only access to the endpoint).
#RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
#ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema = {
    'key': {
        'type': 'string'
    },
    'name':{
        'type': 'string'
    },
    'location': {
        'type': 'string'
    },
    'time': {
        'type': 'number'
    }
}

people = {
    'schema': schema
}

DOMAIN = {
    'people': people,
}

