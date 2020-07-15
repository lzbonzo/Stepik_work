import csv
import re
crimes = []
max = 0

with open('Crimes.csv') as f:
    table = csv.DictReader(f)
    for row in table:
        if '2015' in row['Date']:
            crimes.append(row['Primary Type'])
for elem in crimes:
    if crimes.count(elem) > max:
        max = crimes.count(elem)
        max_crimes = elem

print(max_crimes)