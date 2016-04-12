from lxml import html
from os.path import join
import json

STORAGE_DIR = 'storage'
STORED_PAGE_NAME = join(STORAGE_DIR, 'homepage.html')

WRANGLED_DIR = 'wrangled'
WRANGLED_DATA_NAME = join(WRANGLED_DIR, 'millionpixels.json')

with open(STORED_PAGE_NAME, 'r') as rf:
    txt = rf.read()

doc = html.fromstring(txt)


IMG_HEIGHT = 1000

things = []
for element in doc.cssselect('map > area'):
    atts = element.attrib
    d = dict()
    d['title'] = atts['title']
    d['href'] = atts['href']
    coords = atts['coords'].split(',')

    d['uid'] = 'x'.join([c.rjust(4, '0') for c in coords])
    d['imagemap_coords'] = [int(c) for c in coords]
    # calculate bounding box using standard coordinate system
    lt, ya, rt, yb = d['imagemap_coords']
    bt = IMG_HEIGHT - yb
    tt = IMG_HEIGHT - ya
    d['bbox'] = [lt, bt, rt, tt]
    d['width'] = rt - lt
    d['height'] = tt - bt
    d['area'] = d['width'] * d['height']
    things.append(d)
