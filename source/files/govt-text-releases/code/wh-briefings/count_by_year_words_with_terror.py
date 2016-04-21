from glob import glob
from os.path import join
from collections import defaultdict
import json

from settings import BRIEFS_JSON_DIR


def count_matching_words(datadict, pattern):
    x = 0
    for word, wordcount in datadict['word_counts'].items():
        if pattern in word:
            x += wordcount
    return x


tally = defaultdict(int)
filenames = glob(join(BRIEFS_JSON_DIR, '*.json'))
for fn in filenames:
    with open(fn, 'r') as rf:
        data = json.load(rf)
    yr = data['date'][0:4]
    tally[yr] += count_matching_words(data, 'terror')



print("Words with terror:")
years = sorted(tally.keys())
for yr in years:
    ct = tally[yr]
    print("{year}: {count}".format(year=yr, count=ct))
