from bs4 import BeautifulSoup
import requests 
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time

url = "https://news.v.daum.net/v/20201218155209140"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

#BS4
res =requests.get(url, headers=headers)
res.raise_for_status()
print(res.raise_for_status())
soup = BeautifulSoup(res.text, "lxml")

#댓글 attrs
# .find("div", attrs={"class":"cmt_info"}).
comments = soup.find("strong", attr={"class":"tit__nick"})
print(comments)
# comment = comments[1].p["desc_txt font_size_17"]
# print(comment)
"""for comment in comments:
    cmt = comment
    print(cmt)"""


#selenium
# driver = webdriver.Chrome(ChromeDriverManager().install())
# browser = webdriver.Chrome("C:\\Python\\chromedriver.exe")

# browser.maximize_window() #창 최대화

# browser.get(url)


#더보기 선택 + 클릭
# time.sleep(5)
# browser.find_element_by_xpath("//*[@id='alex-area']/div/div/div/div[3]/div[3]").click()
# time.sleep(5)

#스크롤 과정
# SCROLL_PAUSE_TIME = 5
# last_height = browser.execute_script("return document.body.scrollHeight")
"""
일단 보류
while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    
    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height"""

#댓글 긁어오기