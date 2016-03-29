

Get list

~~~sh
curl -L 'https://docs.google.com/spreadsheets/d/106bbZ1mFFqYeWF06ggeKLmeLA0PXhIldvsz5o8htQ9E/export?format=csv&id=106bbZ1mFFqYeWF06ggeKLmeLA0PXhIldvsz5o8htQ9E&gid=1061813612' | 
  csvjson --indent 2 > data/challenges.json
~~~


~~~py
import json
import csv
j = open('data/challenges.json', 'w')
with open("data/challenges.csv") as c:
    rows = list(csv.DictReader(c))
    json.dump(rows, j, indent=2)
~~~
