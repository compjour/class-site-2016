from os import makedirs
from os.path import join, exists
import json
import requests
DATA_DIR = 'mydata'
makedirs(DATA_DIR, exist_ok=True)
SOURCE_URL = 'http://www.saferproducts.gov/RestWebServices/Recall'
DATA_FILENAME = join('mydata', 'saferproducts-recalls-2016.json')



def get_data():
    if not exists(DATA_FILENAME):
        print("Downloading", SOURCE_URL, 'and saving to', DATA_FILENAME)
        resp = requests.get(SOURCE_URL, params={'format': 'json', 'RecallDateStart': 2016})
        with open(DATA_FILENAME, 'w') as wf:
            wf.write(resp.text)
            txt = resp.text
    else:
        with open(DATA_FILENAME, 'r') as rf:
            txt = rf.read()
    return json.loads(txt)
