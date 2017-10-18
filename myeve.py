from eve import Eve


def post_get(resource, request, payload):
    print('a get on "%s" performed with payload %s returned.' % (resource, payload.data))


def pre_get(resource, request, lookup):
    print('a get on resource %s with request %s and lookup %s.' % (resource, request, lookup))
    lookup["key"] = {'$eq': 'gd'}

app = Eve()
app.on_post_GET += post_get
app.on_pre_GET += pre_get

app.run()
