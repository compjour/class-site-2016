from os import makedirs
from os.path import join

INDEX_PAGES_DIR = join('mydata', 'index-pages')
makedirs(INDEX_PAGES_DIR, exist_ok=True)

BRIEFS_DIR = join('mydata', 'briefs')
makedirs(BRIEFS_DIR, exist_ok=True)

BRIEFS_JSON_DIR = join('mydata', 'briefs-json')
makedirs(BRIEFS_JSON_DIR, exist_ok=True)


IMAGES_DIR = 'myvizzes'
makedirs(IMAGES_DIR, exist_ok=True)
