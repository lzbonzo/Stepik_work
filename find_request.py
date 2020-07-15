import requests
import re

def link_check(link):
    link_req = requests.get(link)
    links_check = re.findall(r"href=(.*html\")", str(link_req.content))
    if link in links_check:
        print('Yes')
    else:
        print('No')


line_a = "https://stepic.org/media/attachments/lesson/24472/sample2.html"
line_b = "https://stepic.org/media/attachments/lesson/24472/sample2.html"
#print(type(line_a))
line_a_req = requests.get(line_a)
#print(line_a_req.content)
links = re.findall(r"href=\"(.*html)\"", line_a_req.text)

res = 'No'
test = []
#print(links)
for link in links:
   #print(link)
   #print(type(link))
   u = requests.get(link)

   for elem in re.findall(r"href=\"(.*html)\"", u.text):
       test.append(elem)


   if line_b in test:
       res = "Yes"


#print(test)
print(res)