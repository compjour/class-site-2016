from glob import glob
from os.path import join
import json
from settings import BRIEFS_JSON_DIR

filenames = glob(join(BRIEFS_JSON_DIR, '*.json'))

terror_words = 0
for fn in filenames:
    with open(fn, 'r') as rf:
        data = json.load(rf)

    for word, wordcount in data['word_counts'].items():
        if 'terror' in word:
            terror_words += wordcount

print("Words with terror:", terror_words)
