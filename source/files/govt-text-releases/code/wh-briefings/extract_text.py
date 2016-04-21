from bs4 import BeautifulSoup
from collections import Counter, OrderedDict
from glob import glob
from os.path import basename, join
from os import makedirs
import re
import json

from settings import BRIEFS_DIR, BRIEFS_JSON_DIR

WORD_PATTERN = re.compile(r"[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+")


briefnames = glob(join(BRIEFS_DIR, '*.html'))
for idx, bn in enumerate(briefnames):
    print(bn, "{}/{}".format(idx, len(briefnames)))
    with open(bn) as rf:
        soup = BeautifulSoup(rf.read(), 'lxml')

    mydata = OrderedDict()
    title_el = soup.find('meta', {'property':'og:title'})
    date_el = soup.find('meta', {'property':'article:published_time'})
    link_el = soup.find('link', {'rel': 'canonical'})
    mydata['title'] = title_el['content']
    mydata['date'] = date_el['content']
    mydata['url'] = link_el['href']
    bodycontent = soup.select_one('#content-start').select_one('div.field-items')
    bodytext = bodycontent.text.lower()
    wordtokens = WORD_PATTERN.findall(bodytext.lower())
    mydata['total_words'] = len(wordtokens)
    mydata['word_counts'] = OrderedDict(Counter(wordtokens).most_common())

    jname = join(BRIEFS_JSON_DIR, basename(bn) + '.json')
    with open(jname, 'w') as f:
        f.write(json.dumps(mydata, indent=2))

