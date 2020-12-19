import requests
from bs4 import BeautifulSoup as bs

result = []
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
url = " https://comment.daum.net/apis/v1/ui/single/main/@20201218202102673"
headers.update({
    "Authorization" : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb3J1bV9rZXkiOiJuZXdzIiwiZ3JhbnRfdHlwZSI6ImFsZXhfY3JlZGVudGlhbHMiLCJzY29wZSI6W10sImV4cCI6MTYwODM1MjQwNSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9DTElFTlQiXSwianRpIjoiOTljYjE2M2YtNjAwZS00NDhmLWI5NjEtODhhZTFjYmVmYTkxIiwiZm9ydW1faWQiOi05OSwiY2xpZW50X2lkIjoiMjZCWEF2S255NVdGNVowOWxyNWs3N1k4In0.XFH36e5zuJhqIk29LKBlqyVYKOGINvdu4fuJuTfXOkY"

})
res = requests.get(url, headers=headers)
"""
if res.status_code == 200:
    json_data = res.json()
    for d in json_data:
        print(d['content'])
else:
    print(res)
"""
if res.status_code == 200:
    json_data = res.json()
    print(f'id : {json_data["id"]}')
    print(f'title : {json_data["title"]}')
    url = "https://comment.daum.net/apis/v1/posts/151767724/comments?parentId=0&offset=0&limit=3&sort=POPULAR&isInitial=true&hasNext=true&randomSeed=1608310551"
    res = requests.get(url.format(json_data[id]))
    json_data = res.json()
    for d in json_data:
        print(d['content'])
else: 
    print(res)