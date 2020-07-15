import requests
import re


site_pattern = re.compile(r'<a.*?href=[\'\"](?:[\w]+:\/\/)?(\w[\w\.-]+).*>')
url = input()
site = requests.get(url).text
#print(site_pattern.findall(site))



#with open('URLS.html') as f:
   # site = f.readlines()
#r'<a.*?href=[\'\"]\/?(?!\.\.)(.*)[\'\":/]>'

sites = set()
sites_res = set()
for elem in site_pattern.findall(site):
    #print(elem)
    sites.add(elem)

for elem in sorted(sites):
    print(elem)

'''

for url in textsss:
    print(site_pattern.findall(url))
    site = url.strip()
    for elem in site_pattern.findall(url):
        sites.add(elem)
'''

