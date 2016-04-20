from settings import *
from bs4 import BeautifulSoup
from glob import glob
from os.path import basename, join, splitext
from urllib.parse import urljoin


# Download all mugshots
# assuming inmate pages are downloaded
for fn in glob(join(INMATE_PAGES_DIR, '*.html')):
    with open(fn, 'r') as rf:
        soup = BeautifulSoup(rf.read(), 'lxml')
    img = soup.find('img', {'alt': 'Picture of Offender'})
    if img:
        url = urljoin(SOURCE_URL_BASE, img['src'])
        # images can be gif or jpg or whatever
        _n, filetype = splitext(basename(url))
        # inmate id comes from the name of the inmate page
        inmate_id = splitext(basename(fn))[0]
        fn = join(MUGSHOT_PAGES_DIR, inmate_id + filetype)
        ez_fetch(url, fn)
