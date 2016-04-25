from flask import Flask
from os import makedirs
import requests
import json
SOURCE_URL = 'http://stash.compjour.org/samples/cpsc/recalls201604.json'

def get_data():
    resp = requests.get(SOURCE_URL)
    txt = resp.text
    datarows = json.loads(txt)
    return datarows


app = Flask(__name__)
recalls_data = get_data()

@app.route("/")
def homepage():
    htmlstr = "<p>The data includes {num} things<p>".format(num=len(recalls_data))
    for row in recalls_data:
        htmlstr += "<p><strong>{title}</strong>: {url}</p>".format(title=row['Title'], url=row['URL'])
    return htmlstr

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
