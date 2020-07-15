import requests
import json

client_id = '74c13e4e04d2c2bf1169'
client_secret = '902acf4878dfc515a919c3917f344b35'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

params = {'birthday'}

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
with open('dataset_24476_4.txt') as f:
    artists_id = f.readlines()
artists = []
for id in artists_id:
    id = id.strip()
    url = "https://api.artsy.net/api/artists/" + id
    r = requests.get(url, headers=headers)
    j = json.loads(r.text)
    artists.append(j['birthday'] + ' ' + j['sortable_name'])

with open('output.txt', 'w') as w:
    for elem in sorted(artists):
        w.write(elem[5:] + '\n')
