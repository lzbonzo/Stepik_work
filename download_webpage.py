from urllib.request import urlopen
import requests
import re
q = urlopen("https://ru.wikipedia.org/wiki/%D0%AF%D0%B7%D1%8B%D0%BA_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F").read()
#q = re.search('C\+\+',wik)
q = str(q)
if q.count('C++') > q.count('Python'):
    print('C++')
else:
    print('Python')
print(q)