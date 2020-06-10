from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch(
    cloud_id="testH-JV:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJDg4MWUzNGIwYWRlNzQyNTJhMTg5YjI5ZTIyOTk4NzQzJDQ4NjA1NzIzNGI1YTQ0NjI5ZDc3MTE4NTc3MWRkMzhl",
    http_auth=("elastic", "XPDnUnEbJhqNMcTlRaPKI1MB"),
)

# doc = {
#     'author': 'kimchy2',
#     'text': 'Elasticsearch: cool. bonsai cool 2222.',
#     'timestamp': datetime.now(),
# }
# res = es.index(index="my-index", id=1, body=doc)
# print(res['result'])

# res = es.get(index="my-index", id=1)
# print(res['_source'])

# es.indices.refresh(index="my-index")

# res = es.search(index="my-index", body={"query": {"match_all": {}}})
# print("Got %d Hits:" % res['hits']['total']['value'])
# for hit in res['hits']['hits']:
#     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

# create an index in elasticsearch, ignore status code 400 (index already exists)
es.indices.create(index='my-ind', ignore=400)
{'acknowledged': True, 'shards_acknowledged': True, 'ind': 'my-ind'}

# datetimes will be serialized
es.index(index="my-ind", id=42, body={"any": "data", "timestamp": datetime.now()})
{'_index': 'my-index-2',
 '_type': '_docccc',
 '_id': '42',
 '_version': 1,
 'result': 'created',
 '_shards': {'total': 2, 'successful': 1, 'failed': 0},
 '_seq_no': 0,
 '_primary_term': 1}

# but not deserialized
es.get(index="my-ind", id=42)['_source']
{'any': 'data', 'timestamp': '2019-05-17T17:28:10.329598'}
