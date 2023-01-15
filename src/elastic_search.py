import sys, json
import logging
from elasticsearch import Elasticsearch

client = Elasticsearch(hosts=["https://cs172-80a738.es.us-west1.gcp.cloud.es.io:9243"], http_auth =('elastic', 'g3RTWawioggWM3aGHzLn7Q34'))

index_name = "html_index"

query_request = "empowering"

doc_body = {
    "query": {
        "match": {
            "html": query_request
        }
    }
}

output = client.search(index=index_name, body =doc_body)

total_hits = output["hits"]["hits"]
#print("total hits:", len(output["hits"]["hits"]))
print("total hits:", len(total_hits))

for num, doc in enumerate(total_hits):
    print ("DOC ID: ", doc["_id"],doc["_score"], "\n")

# def connect_elasticsearch():
#     _es = None
#     _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
#     if _es.ping():
#         print('Yay Connect')
#     else:
#         print('Awww it could not connect!')
#     return _es

# if __name__ == '__main__':
#   logging.basicConfig(level=logging.ERROR)
