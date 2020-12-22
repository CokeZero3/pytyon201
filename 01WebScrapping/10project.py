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

#날짜 구하기
now = datetime.now()
# print(now.year, now.month, now.day)

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8" 
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

#1. 오늘의 날씨 구하기
temp = soup.find("span", attrs={"class":"todaytemp"}).get_text()
max_temp = soup.find("span", attrs={"class":"max"}).get_text()
min_temp = soup.find("span", attrs={"class":"min"}).get_text()
weather = soup.find("p", attrs={"class":"cast_txt"}).get_text()
am_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).find("span", attrs={"class":"rain_rate wet"}).get_text()
pm_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).find("span", attrs={"class":"rain_rate"}).get_text()
lv1 = soup.find("dd", attrs={"class":"lv1"}).get_text() # 오존지수
lv2 = soup.find("dd", attrs={"class":"lv2"}).get_text() # 미세먼지
lv3 = soup.find("dd", attrs={"class":"lv3"}).get_text() # 초미세먼지


print("[{}년 {}월 {}일, 오늘의 날씨]".format(now.year, now.month, now.day))
print(weather)
print("현재 {}˚C (최저 {}/ 최고 {})".format(temp, min_temp, max_temp))
print("오전 {} / 오후 {}".format(am_rain_rate, pm_rain_rate))

print("미세먼지 {}".format(lv2))
print("초미세먼지 {}".format(lv3))
print("오존지수 {}".format(lv1))
print("="*50)