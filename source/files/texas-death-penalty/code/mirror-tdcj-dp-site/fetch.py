from bs4 import BeautifulSoup
from os.path import join, basename, splitext, exists
from os import makedirs
from urllib.parse import urljoin
from glob import glob

from settings import *



# Download the index pages first
for _pg in SOURCE_URL_PAGES:
    url = urljoin(SOURCE_URL_BASE, _pg)
    fn = join(INDEX_PAGES_DIR, basename(url))
    ez_fetch(url, fn)



# Download all inmate pages...
# assuming index pages are downloaded
for fn in glob(join(INDEX_PAGES_DIR, '*.html')):
    with open(fn, 'r') as rf:
        soup = BeautifulSoup(rf.read(), 'lxml')
        # figure out which column corresponds to TDCJ number
        tdcj_col_idx = 0
        header_titles = [t.text for t in soup.select('table th')]
        tdcj_col_idx = header_titles.index('TDCJ Number')
        for inmate_row in soup.find_all('tr'):
            if inmate_row.find_all('td'): # make sure it's a real row, not header row
               idcol = inmate_row.find_all('td')[tdcj_col_idx]
               inmate_id = idcol.text
               for atag in inmate_row.find_all('a'):
                    if 'Offender Information' in atag.text and 'no_info_available' not in atag['href']:
                        url = urljoin(SOURCE_URL_BASE, atag['href'])
                        _n, filetype = splitext(basename(url))
                        # ignore the name of the file
                        fn = join(INMATE_PAGES_DIR, inmate_id + filetype)
                        ez_fetch(url, fn)



# Download all mugshots
# assuming inmate pages are downloaded
for fn in glob(join(INMATE_PAGES_DIR, '*.html')):
    with open(fn, 'r') as rf:
        soup = BeautifulSoup(rf.read(), 'lxml')
        img = soup.find('img', {'alt': 'Picture of Offender'})
        if img:
            url = urljoin(SOURCE_URL_BASE, img['src'])
            _n, filetype = splitext(basename(url))
            inmate_id = splitext(basename(fn))[0]
            fn = join(MUGSHOT_PAGES_DIR, inmate_id + filetype)
            ez_fetch(url, fn)

# Download all lastwords pages...
# assuming index pages are downloaded
for fn in glob(join(INDEX_PAGES_DIR, '*.html')):
    with open(fn, 'r') as rf:
        soup = BeautifulSoup(rf.read(), 'lxml')
        # figure out which column corresponds to TDCJ number
        tdcj_col_idx = 0
        header_titles = [t.text for t in soup.select('table th')]
        tdcj_col_idx = header_titles.index('TDCJ Number')
        for inmate_row in soup.find_all('tr'):
            if inmate_row.find_all('td'): # make sure it's a real row, not header row
               idcol = inmate_row.find_all('td')[tdcj_col_idx]
               inmate_id = idcol.text
               for atag in inmate_row.find_all('a'):
                    if 'Last Statement' in atag.text and 'no_last_statement' not in atag['href']:
                        url = urljoin(SOURCE_URL_BASE, atag['href'])
                        _n, filetype = splitext(basename(url))
                        # ignore the name of the file
                        fn = join(LASTWORDS_PAGES_DIR, inmate_id + filetype)
                        ez_fetch(url, fn)
