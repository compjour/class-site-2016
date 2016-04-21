import requests
from os import makedirs
from os.path import join
from settings import INDEX_PAGES_DIR

URL_ENDPOINT = 'https://www.whitehouse.gov/briefing-room/press-briefings'
MAX_PAGE_NUM = 162

for pagenum in range(0, MAX_PAGE_NUM):
    resp = requests.get(URL_ENDPOINT, params={'page': pagenum})
    print("Downloaded", resp.url)

    fname = join(INDEX_PAGES_DIR, '{}.html'.format(pagenum))
    print("Saving to", fname)
    with open(fname, "w") as wf:
        wf.write(resp.text)
