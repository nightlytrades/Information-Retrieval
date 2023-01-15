# save this as app.py
from typing import Counter
from flask import Flask, render_template, request
from elasticsearch import Elasticsearch
from flask.helpers import url_for
import requests
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/')
def home():

    return render_template('site.html')


@app.route('/', methods=['GET', "POST"])
def query_req():

    return redirect(url_for("results"), numhits=num_hits)


@app.route('/results', methods=["GET"])
def results():

    doc_id = []

    # temp = requests.args.post(num_hits)
    query_request = request.args.get('search')
    client = Elasticsearch(hosts=["https://cs172-80a738.es.us-west1.gcp.cloud.es.io:9243"],
                           http_auth=('elastic', 'g3RTWawioggWM3aGHzLn7Q34'))
    index_name = "html_index"

    doc_body = {
        "query": {
            "match": {
                "html": query_request
            }
        }
    }
    output = client.search(index=index_name, body=doc_body)

    total_hits = output["hits"]["hits"]
    counter = 0
    for num, doc in enumerate(total_hits):
        counter = counter+1

        doc_id.append(str(counter) + " --- " + "DOC ID:" +
                      doc["_id"] + " --- " + "Score: " + str(doc["_score"]))

    return render_template('results.html', results=doc_id)


if __name__ == '__main__':
    app.run(debug=True)
