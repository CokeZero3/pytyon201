import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res =requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# cartoons = soup.find_all("a", attrs={"class":"title"})
# for cartoon in cartoons:
#     print(cartoon.get_text())

cartoons = soup.find_all("td", attrs={"class":"title"})

title = cartoons[0].a.get_text()
link = cartoons[0].a["href"]
print(title, "https://comic.naver.com"+link)
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com"+cartoon.a["href"]
    print(title, link)