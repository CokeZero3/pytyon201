from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser = webdriver.Chrome("C:\\Python\\chromedriver.exe")
browser.maximize_window()

#페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 스크롤 내리기 
# 모니터 해상도 높이인 1080만큼 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)") #1920 X 1080
# browser.execute_script("window.scrollTo(0, 2080)") 

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")


# 2초에 한번씩 스크롤 내리기를 위함
import time
interval = 2

# 현쟈 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

#반복수행
while True:
    #스크롤 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #페이지 로딩 대기
    time.sleep(interval)
    #현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    
    if curr_height == prev_height:
        break
    
    prev_height = curr_height
    
print(" 스크롤 완료")

import requests
from bs4 import BeautifulSoup

"""
필요없엉
url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
    }

res = requests.get(url, headers=headers)
res.raise_for_status()
"""
soup = BeautifulSoup(browser.page_source, "lxml")
 
# movies = soup.find_all("div", attrs={"class": ["ImZGtf mpg5gc", "Vpfmgd"]}) #클래스를 리스트로 만들어서 둘 다 가져오게 맨들기
movies = soup.find_all("div", attrs={"class": "Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    
    #할인 전 가격
    original_price =movie.find("span", attrs={"class": "SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, "<할인되지 않은 영화 제외>")
        continue
    
    #할인된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    #링크
    url = movie.find("a", attrs={"class":"JC71ub"})["href"] #https://play.google.com + url
    
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액: {price}")
    print("링크 : ", "https://play.google.com"+ url)
    print("="*120)
    
