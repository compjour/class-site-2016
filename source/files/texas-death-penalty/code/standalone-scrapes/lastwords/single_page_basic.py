from bs4 import BeautifulSoup
import requests
SOURCE_URL = 'http://www.tdcj.state.tx.us/death_row/dr_info/wardadamlast.html'


resp = requests.get(SOURCE_URL)
soup = BeautifulSoup(resp.text, 'lxml')

# get the node with the Last Statement content
el = soup.find('p', text='Last Statement:')
# all other subsequent sibling nodes should have the right text
lastwords = ""
for p in el.find_next_siblings('p'):
    lastwords += p.text

# All done with extracting last words...let's try to get their name
offel = soup.find('p', text="Offender:")
# by definition, the next sibling p tag contains the name
offender = offel.find_next_sibling('p').text

print(offender)
print(lastwords)
