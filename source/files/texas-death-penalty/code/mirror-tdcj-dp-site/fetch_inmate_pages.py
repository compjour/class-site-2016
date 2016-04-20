from settings import *
from bs4 import BeautifulSoup
from glob import glob
from os.path import join
from urllib.parse import urljoin

def extract_tdcj_column_index(soup):
    # simply returns an integer, representing the index
    # of the table column in which 'TDCJ Number' can be found
    idx = 0
    header_titles = [t.text for t in soup.select('table th')]
    return header_titles.index('TDCJ Number')


# Download all inmate pages...
# assuming index pages are downloaded
for fn in glob(join(INDEX_PAGES_DIR, '*.html')):
    with open(fn, 'r') as rf:
        soup = BeautifulSoup(rf.read(), 'lxml')
    tdcj_col_idx = extract_tdcj_column_index(soup)

    for inmate_row in soup.find_all('tr'):
        if inmate_row.find_all('td'): # make sure it's a real row, not header row

           # now that we're on an inmate row, extract the ID number from
           # the appropriate column
           idcol = inmate_row.find_all('td')[tdcj_col_idx]
           inmate_id = idcol.text.strip()


           # select the first (and only) a tag for each row that has
           # text == 'Offender Information'
           inmate_link = inmate_row.find('a', text='Offender Information')
           if inmate_link:
                if 'no_info_available' not in inmate_link['href']:
                    url = urljoin(SOURCE_URL_BASE, inmate_link['href'])
                    # since we already have the inmate id, we
                    # can use that for the file name

                    # however we have to extract the file extension from the
                    # URL, because not all inmate pages are HTML...some
                    # are jpg scans...
                    _n, filetype = splitext(basename(url))
                    fn = join(INMATE_PAGES_DIR, inmate_id + filetype)
                    ez_fetch(url, fn)
