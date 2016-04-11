from os.path import exists
import requests
DATA_URL = 'http://unitedstates.sunlightfoundation.com/legislators/legislators.csv'
DATA_FILENAME = 'legislators.csv'

def fetch_data():
    if exists(DATA_FILENAME):
        print("Already downloaded", DATA_FILENAME)
    else:
        print("Downloading from", DATA_URL)
        resp = requests.get(DATA_URL)
        with open(DATA_FILENAME, 'w') as wf:
            msg = "Saving {numchars} to: {filename}"
            print(msg.format(numchars=len(resp.text), filename=DATA_FILENAME))
            wf.write(resp.text)

def read_data():
    fetch_data()
    with open(DATA_FILENAME, 'r') as rf:
        txt = rf.read()
    return txt



if __name__ == '__main__':
    fetch_data()
