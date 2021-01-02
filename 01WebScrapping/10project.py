# 1. [오늘의 날씨]
# 흐림, 어제보다 00도 높아요
# 현재 00'c (최저00/최고00)
# 오전 강수확률 0% / 오후 강수확률 00%
# 미세먼지 00/m 좋음
# 초미세먼지 00/m 좋음

# 2.[헤드라인 뉴스]
# 1 ~ 3 
# 3. [IT 헤드라인 뉴스]
# 1 ~ 3 


from bs4 import BeautifulSoup
import requests
from datetime import datetime
import re

#나도코딩 방법
def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup
def print_news(index, title, link):
        print("{}. {}".format(index+1, title))
        print(" (링크: {})".format(link))
        
def scrape_weather():
    now = datetime.now()
    print("[{}년 {}월 {}일, 오늘의 날씨]".format(now.year, now.month, now.day))
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8" 
    soup = create_soup(url)
  
    
    # temp = soup.find("span", attrs={"class":"todaytemp"}).get_text() #
    curr_temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨", "")
    max_temp = soup.find("span", attrs={"class":"max"}).get_text() #최저 온도
    min_temp = soup.find("span", attrs={"class":"min"}).get_text() #최고 온도
    weather = soup.find("p", attrs={"class":"cast_txt"}).get_text()

    #오전 강수 확률, 오후 강수확률
    am_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip()
    pm_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip()
    
    # dust = soup.find("dl", attrs={"class":"indicator"}, text=["미세먼지", "초미세먼지"]).get_text() # 미세먼지
    dust = soup.find("dl", attrs={"class":"indicator"}) # 미세먼지
    pm10 = dust.find_all("dd")[0].get_text()
    pm25 = dust.find_all("dd")[1].get_text()
    ozone = dust.find_all("dd")[2].get_text()
    
    #출력 
    print(weather)
    print("현재 {}˚C (최저 {}/ 최고 {})".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후 {}".format(am_rain_rate, pm_rain_rate))
    print()
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))
    print("오존지수 {}".format(ozone))

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url ="http://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)
    
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print_news(index, title, link)       
    print()       
    

def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class","type06_headline"}).find_all("li", limit=3)
    for index, news in enumerate(news_list):
        a_idx=0
        img = news.find("img")
        if img:
            a_idx = 1 # img 태그가 있으면 1번째 a 태그의 정보를 사용
        
        atag= news.find_all("a")[a_idx]
        title = news.find("a")[a_idx].get_text().strip()
        link = url + news.find("a")["href"]
        print_news(index, title, link)
    print()
    
def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")}) #re.compile("") 정규식 모듈로 "" 시작하는 무언가 찾는 코드 
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2]: # 8문장이 있다고 가정할 때, index 기준 4~7까지 잘라서 가져옴
        print(sentence.get_text().strip())
        
    print("한글 지문")
    for sentence in sentences[:len(sentences)//2]: # 8문장이 있다고 가정할 때, index 기준 0~3까지 잘라서 가져옴
        print(sentence.get_text().strip())
    

if __name__ == "__main__":
    scrape_weather() #오늘의 날씨 정보 가져오기
    scrape_headline_news() #헤드라인 뉴스
    scrape_it_news() #IT 뉴스 정보 가져오기
    scrape_english()
    