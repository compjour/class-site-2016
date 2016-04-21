from bs4 import BeautifulSoup
from glob import glob
from os import makedirs
from os.path import join
from urllib.parse import urljoin
import requests

from settings import INDEX_PAGES_DIR, BRIEFS_DIR

WH_PB_HOME_URL = 'https://www.whitehouse.gov/briefing-room/press-briefings'
# Gather up all the index pages
html_filenames = glob(join(INDEX_PAGES_DIR, '*.html'))

# for each index page
for hname in html_filenames:
    # open and parse it as HTML
    with open(hname, 'r') as rf:
        txt = rf.read()
        soup = BeautifulSoup(txt, 'lxml')
    # now select for <a> tags nested within <h3> tags
    for hed in soup.find_all('h3'):
        href = hed.find('a').attrs['href']
        url = urljoin(WH_PB_HOME_URL, href)
        print("Downloading from...\n", url)
        resp = requests.get(url)
    # create a filename from the relative href path
        fn = href.replace('/', '-').strip('-') + '.html'
        full_fname = join(BRIEFS_DIR, fn)
        print("Saving to...\n", full_fname)
        with open(full_fname, 'w') as wf:
            wf.write(resp.text)
