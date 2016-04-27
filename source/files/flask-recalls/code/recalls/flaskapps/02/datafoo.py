import json
import requests
SOURCE_URL = 'http://stash.compjour.org/samples/cpsc/recalls201604.json'


def get_data():
    resp = requests.get(SOURCE_URL)
    return json.loads(resp.text)
