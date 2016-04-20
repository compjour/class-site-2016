from os.path import join, basename, splitext, exists
from os import makedirs
import requests

SOURCE_URL_BASE = 'https://www.tdcj.state.tx.us/death_row/'

DATA_DIR = 'mydata'
INDEX_PAGES_DIR = join(DATA_DIR, 'index-pages')
INMATE_PAGES_DIR = join(DATA_DIR, 'inmate-pages')
MUGSHOT_PAGES_DIR = join(DATA_DIR, 'mugshots')
LASTWORDS_PAGES_DIR = join(DATA_DIR, 'lastwords')
INMATE_JSON_DIR = join(DATA_DIR, 'inmate-json')


makedirs(INDEX_PAGES_DIR, exist_ok=True)
makedirs(INMATE_PAGES_DIR, exist_ok=True)
makedirs(MUGSHOT_PAGES_DIR, exist_ok=True)
makedirs(LASTWORDS_PAGES_DIR, exist_ok=True)
makedirs(INMATE_JSON_DIR, exist_ok=True)


def ez_fetch(url, filename):
    print("---------")
    if exists(filename):
        print("Already downloaded:", url)
        print("Into:", filename)
    else:
        print("Currently downloading:", url)
        print("Into:", filename)
        resp = requests.get(url)
        with open(filename, 'wb') as wf:
            wf.write(resp.content)
