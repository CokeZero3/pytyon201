import csv
import requests
from bs4 import BeautifulSoup

url = "https://news.daum.net/ranking/bestreply"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

#다음 댓글 많은 - 뉴스 제목
news_title = soup.find_all("div", attrs={"cont_thumb"})
news_press = soup.find_all("span",attrs={"class":"info_news"})
#뉴스 제목 출력 확인
title = news_title[0].a.get_text()
# print(title)

# for i in range(1, 50):
#     print(news_press[i].get_text())

# for news in news_title:
#     title = news.a.get_text()
#     link = news.a["href"]
#     press = news.span[""]
    
#     print("제목: {} || 링크: {} ".format(title, link))

# 빈 리스트 생성 - 링크 리스트  
links = []

#리스트 append 시키기

for news in news_title:
    link = news.a["href"]
    links.append(link)

print(len(links))
print(links[1])

# for news in news_title:
#     link = news.a["href"]
#     links.append(link)
    
#     links
    

    

    
    
