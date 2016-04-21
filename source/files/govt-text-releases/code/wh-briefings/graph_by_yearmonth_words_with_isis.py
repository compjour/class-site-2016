from glob import glob
from os.path import join
from collections import defaultdict
import datetime
import json
import matplotlib.pyplot as plt
import re

from settings import BRIEFS_JSON_DIR, IMAGES_DIR


PATTERN_TO_CHECK = r'\bisis|isil\b'

def count_matching_words(datadict, pattern):
    x = 0
    for word, wordcount in datadict['word_counts'].items():
        if re.search(pattern, word):
            x += wordcount
    return x


tally = defaultdict(int)
filenames = glob(join(BRIEFS_JSON_DIR, '*.json'))
for fn in filenames:
    with open(fn, 'r') as rf:
        data = json.load(rf)
    dt = data['date'][0:7]
    tally[dt] += count_matching_words(data, PATTERN_TO_CHECK)


sorted_tally = sorted(tally.items(), key=lambda x: x[0])


dates = []
for p in sorted_tally:
    yr, month = p[0].split('-')
    dates.append(datetime.datetime(int(yr), int(month), 1))

words = [p[1] for p in sorted_tally]

plt.bar(dates, words)
plt.savefig(join(IMAGES_DIR, 'isis-yearmonth.png'))
