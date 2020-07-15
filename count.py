'''

import requests
with open('dataset_3378_3.txt') as inf:
    ur = inf.readline().strip()
hur = 'https://stepic.org/media/attachments/course67/3.6.3/'
q = requests.get(ur)
while q.text[0:2] != 'We':
    ur = hur + q.text
    #print(ur)
    q = requests.get(ur)

with open('output.txt', 'w') as ouf:
    ouf.write(q.text)
'''
DICT = {'a' : ['q', 'c'], 'b' : ['j', 'c']}
if 'q' in DICT['b']:
    print('dfd')