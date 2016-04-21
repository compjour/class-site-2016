from glob import glob
from os.path import join
import json

from settings import BRIEFS_JSON_DIR

filenames = glob(join(BRIEFS_JSON_DIR, '*.json'))

terror_words = 0
for fn in filenames:
    with open(fn, 'r') as rf:
        data = json.load(rf)
    wc = data['word_counts'].get('terror')
    # no guarantee that speech mentions ebola
    if wc:
        terror_words += wc

print("Terror words", terror_words)
