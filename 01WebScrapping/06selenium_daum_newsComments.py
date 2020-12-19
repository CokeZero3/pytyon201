from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

url = "https://news.v.daum.net/v/20201218155209140"

#웹 드라이버
driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome("C:\\Python\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get(url)

#더보기 계속 클릭하기
while True:
    try:
        more = driver.find_element_by_css_selector("button.link_fold")
        more.click()
        time.sleep(2) #2초 대기
    except:
        break
#댓글 추출

        