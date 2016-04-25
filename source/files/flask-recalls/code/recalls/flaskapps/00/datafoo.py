import json
import requests
URL = 'http://stash.compjour.org/samples/cpsc/recalls201604.json'

def get_data():
    resp = requests.get(URL)
    datarows = json.loads(resp.text)
    return datarows
