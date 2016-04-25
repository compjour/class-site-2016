from collections import Counter
from os import makedirs
from os.path import join
import requests
import json
DATA_DIR = 'mydata'
makedirs(DATA_DIR, exist_ok=True)
SOURCE_URL = 'http://www.saferproducts.gov/RestWebServices/Recall'
FNAME = join('mydata', 'saferproducts-recalls.json')
print("Downloading from", SOURCE_URL, 'saving to', FNAME)
resp = requests.get(SOURCE_URL, params={'format': 'json', 'RecallDateStart': 2016})
with open(FNAME, 'w') as wf:
    wf.write(resp.text)

data = resp.json()
print("Number of records:", len(data))
# frequency count by year
c = Counter(d['RecallDate'][0:4] for d in data)
for z in sorted(c.items()):
    print('%s: %s' % (z[0], str(z[1]).rjust(4)))
