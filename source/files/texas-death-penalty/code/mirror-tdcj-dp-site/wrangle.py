from settings import *
from bs4 import BeautifulSoup
from glob import glob
from os.path import join
import json
import re
from datetime import datetime


def extract_death_table_row_value(coltxt, table_el):
    ptrn = re.compile('\s*' + coltxt + '\s*', re.IGNORECASE)
    el = table_el.find('td', text=ptrn, attrs={'class': ['tabledata_bold_align_right_deathrow', 'tabledata_bold_align_right_unit']})
    return el.find_next_sibling('td').text.strip()


DEATH_TABLE_ATTRIBUTES = {
    'birth_date': 'Date of Birth',
    'race': 'Race',
    'date_received': 'Date Received',
    'date_offense': 'Date of Offense',
    'county_offense': 'County',
    'education': 'Highest Grade',
    'eye_color': 'Eye Color',
    'gender': 'Gender',
    'hair_color': 'Hair Color',
    'height': 'Height',
    'native_county_or_country': 'Native Countr?y',
    'native_state': 'Native State'
}


filenames = glob(join(INMATE_PAGES_DIR, '*.html'))
for idx, fn in enumerate(filenames):
    with open(fn, 'r') as rf:
        soup = BeautifulSoup(rf.read(), 'lxml')
        print(idx, "out of", len(filenames), " -- ", fn)

    table_el = soup.find('table', attrs={'class': 'tabledata_deathrow_table'})
    id_number = splitext(basename(fn))[1] # just the first part of the filename
    mydata = {}
    mydata['tdcj_number'] = id_number
    for key, titletxt in DEATH_TABLE_ATTRIBUTES.items():
        mydata[key] = extract_death_table_row_value(titletxt, table_el)

    # BROKEN
    # print(mydata['birth_date'])
    # mydata['birth_date'] = datetime.strptime(mydata['birth_date'],'%m/%d/%Y').strftime('%Y-%m-%d')

    # save to JSON
    jname = join(INMATE_JSON_DIR, id_number + '.json')
    with open(jname, 'w') as wf:
        wf.write(json.dumps(mydata, indent=2))

#    edval = extract_death_table_row_value('Education Level (Highest Grade Completed)', table_el)
#    print(edval)

