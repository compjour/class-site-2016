from bs4 import BeautifulSoup
from os import makedirs
from os.path import join, basename, exists
from urllib.parse import urljoin
import requests
STASHED_PAGES_DIR = join('mydata', 'lastwordspages')
makedirs(STASHED_PAGES_DIR, exist_ok=True)

SOURCE_INDEX_URL = 'https://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html'
LAST_WORDS_LINK_COL_IDX = 2 # which column/td element the links are in

# get the index page
resp = requests.get(SOURCE_INDEX_URL)
indexsoup = BeautifulSoup(resp.text, 'lxml')

# iterate through each table row
tablerows = indexsoup.find_all('tr')
for tr in tablerows:
    if '</th>' in str(tr):
         continue # a cheapo way of avoiding the headers row
    # grab the column with the link using a hard-coded positional value
    # i.e. the last word links are all in the 3rd column
    xtd = tr.find_all('td')[LAST_WORDS_LINK_COL_IDX]
    # get the anchor tag and extract 'href'
    href = xtd.find('a').attrs['href']

    # another chance to skip, if no statement was given
    if 'no_last_statement' in href:
         continue


    # other wise, let's download
    print("-------------")
    # determine if we've already downloaded this file
    local_fname = join(STASHED_PAGES_DIR, basename(href))
    if exists(local_fname):
        print("Already exists:", local_fname)
    else:
        # else, we need to download it
        url = urljoin(SOURCE_INDEX_URL, href)
        print("Downloading", url)
        resp = requests.get(url)
        print("Writing to", local_fname)
        with open(local_fname, 'w') as wf:
            wf.write(resp.text)
