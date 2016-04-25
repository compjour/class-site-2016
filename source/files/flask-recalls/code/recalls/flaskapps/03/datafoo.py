from os import makedirs
from os.path import join, exists
from datetime import datetime
from dateutil import parser

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
    return clean_data(txt)


def prettify_date_string(datetxt):
    dt = parser.parse(datetxt)
    return dt.strftime("%Y-%m-%d")

def clean_data(txt):
    datarows = json.loads(txt)
    xrows = []
    for row in datarows:
        x = {}
        x['title'] = row['Title']
        x['url'] = row['URL']
        x['recall_date'] = prettify_date_string(row['RecallDate'])
        if row['Images']:
            x['image_url'] = row['Images'][0]['URL']
        if row['Injuries']:
            x['injuries'] = row['Injuries'][0]['Name']
        else:
            x['injuries'] = 'N/A'
        xrows.append(x)
    return xrows



