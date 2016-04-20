from glob import glob
from os.path import join
from bs4 import BeautifulSoup
import re
STASHED_PAGES_DIR = join('mydata', 'lastwordspages')

filenames = glob(join(STASHED_PAGES_DIR, '*.html'))

for fn in filenames:
    # no need for requests, just open it
    print(fn)
    with open(fn, 'r') as rf:
        soup = BeautifulSoup(rf.read(), 'lxml')

    lastwords = ""
    el = soup.find(('p', 'span'), text=re.compile('Last Statement:'))
    for p in el.find_next_siblings('p'):
        lastwords += p.text


    # All done with extracting last words...let's try to get their name
    offel = soup.find(('p', 'span'), text=re.compile("Offender:"))
    # by definition, the next sibling p tag contains the name
    offender = offel.find_next_sibling('p').text

    print("============================================")
    print(offender)
    print(lastwords)



