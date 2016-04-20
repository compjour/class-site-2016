from settings import *
from urllib.parse import urljoin

SOURCE_URL_PATHS = ['dr_offenders_on_dr.html', 'dr_executed_offenders.html']

# Download the index pages first
for _pg in SOURCE_URL_PATHS:
    url = urljoin(SOURCE_URL_BASE, _pg)
    fn = join(INDEX_PAGES_DIR, basename(url))
    ez_fetch(url, fn)
