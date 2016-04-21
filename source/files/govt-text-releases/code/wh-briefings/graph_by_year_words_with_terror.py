from glob import glob
from os.path import join
from collections import defaultdict
import matplotlib.pyplot as plt
import json
from settings import BRIEFS_JSON_DIR, IMAGES_DIR

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


sorted_tally = sorted(tally.items(), key=lambda x: x[0])


years = [p[0] for p in sorted_tally]
words = [p[1] for p in sorted_tally]

plt.bar(years, words)
plt.savefig(join(IMAGES_DIR, 'terror-year.png'))
