from os import makedirs
from os.path import join
import requests

SOURCE_PAGE_URL = 'http://milliondollarhomepage.com/'
SOURCE_IMAGE_URL = 'http://milliondollarhomepage.com/index_files/image-map.png'

STORAGE_DIR = 'storage'
STORED_PAGE_NAME = join(STORAGE_DIR, 'homepage.html')
STORED_IMAGE_NAME = join(STORAGE_DIR, 'image-map.png')

makedirs(STORAGE_DIR, exist_ok=True)




def fetch_files():
    print("Getting homepage HTML from", SOURCE_PAGE_URL)
    resp = requests.get(SOURCE_PAGE_URL)
    with open(STORED_PAGE_NAME, 'w') as wf:
        wf.write(resp.text)

    print("Getting image map from", SOURCE_IMAGE_URL)
    resp = requests.get(SOURCE_IMAGE_URL)
    with open(STORED_IMAGE_NAME, 'wb') as wf:
        wf.write(resp.content)



if __name__ == '__main__':
    fetch_files()
