from lxml import html
from os.path import join
STORAGE_DIR = 'storage'
STORED_PAGE_NAME = join(STORAGE_DIR, 'homepage.html')

with open(STORED_PAGE_NAME, 'r') as rf:
    txt = rf.read()


doc = html.fromstring(txt)

blocks = doc.cssselect('map > area')
len(blocks)
# 3306

# Find the pixel block that belongs to Thinking Juice
colleges_com = next(b for b in blocks if b.attrib['title'] == 'Colleges.com & U. Magazine')

colleges_com.attrib['coords']
# '70,800,240,820'
# x0: 70, y0: 800,
# x1: 240, y1: 820

# Get the biggest pixel expenditure:

def calc_area_pixels(coords):
    x0, y0, x1, y1 = [int(k) for k in coords.split(',')]
    w = x1 - x0
    h = y1 - y0
    return w * h


def calculate_object_size(obj):
    coords = obj.attrib['coords']
    return calc_area(coords)


biggest_block = max(blocks, key=calculate_object_size)
###########
# Top 20 blocks by pixel area
bigblocks = sorted(blocks, key=calculate_object_size, reverse=True)

for block in bigblocks[0:20]:
    atts = block.attrib
    pixels = calc_area_pixels(atts['coords'])
    print(pixels, atts['href'], atts['title'])





# Most common domain/hostnames
from urllib.parse import urlparse

parsed_urls = [urlparse(b.attrib['href']) for b in blocks]
hostnames = [url.netloc.replace('www.', '') for url in parsed_urls]

# How many unique hostnames?
len(set(hostnames))


# Most common hostnames
from collections import Counter
for name, cnt in Counter(hostnames).most_common(10):
    print(name, cnt)



# Biggest hostnames by pixel count
from collections import defaultdict
pixeldict = defaultdict(int)

for b in blocks:
    url = urlparse(b.attrib['href'])
    hostname = url.netloc.replace('www.', '')
    pixeldict[hostname] += calculate_object_size(b)


pixelcounts = sorted(pixeldict.items(), key=lambda o: o[1], reverse=True)

for hostname, pixels in pixelcounts[0:25]:
    print(pixels, hostname)



