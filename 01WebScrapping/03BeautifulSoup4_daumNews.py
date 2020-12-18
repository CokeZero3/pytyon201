import requests
from bs4 import BeautifulSoup

url = "https://news.daum.net/ranking/age"
res = requests.get(url)
print(res.status_code)
# print(res.text)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
# """
# #naver 댓글 많은 랭킹 뉴스
# news_titles = soup.find_all("a", attrs={"class":"list_title.nclicks('RBP.cmtnws')"})

# for news_title in news_titles:
#     print(news_title.get_text())
# """

#20대 여성
age20s = soup.find_all(attrs={"class":"item_age.item_20s", "class":"rank_female", "class":"link_txt"})
news = soup.find_all("span",attrs={"class":"info_news"})
link = soup.find("a", attrs={"class", "link_txt"})["href"]

for i in range(0, 5):
    print("제목: "+age20s[i].get_text() + "\n언론사:"+news[i].get_text()+"\n바로가기:"+link )
print("\b")    
"""
#20대 남성
age20s = soup.find_all(attrs={"class":"item_age.item_20s", "class":"rank_male", "class":"link_txt"})
news = soup.find_all("span",attrs={"class":"info_news"})
for i in range(0, 5):
    print("제목: "+age20s[i].get_text() + "\n언론사:"+news[i].get_text())
    
"""
    
# """
# news_titles = soup.find_all("li", attrs={"class":"num_news.num"})
# # news_titles = soup.find("a":text="산타가 선물 대신 코로나를..벨기에 요양원서 75명 집단")


# for news_title in news_titles:
#     print(news_title.a.get_text())
#     """