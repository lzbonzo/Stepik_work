import requests

with open('dataset_24476_3.txt') as f:
    number = f.readlines()

with open('output.txt', 'w') as w:
    for n in number:
        n = n.strip()
        url = 'http://numbersapi.com/'+ n + '/math?json'
        res = requests.get(url)
        if res.json()['found']:
            w.write('Interesting\n')
        else:
            w.write('Boring\n')
print('Successful')