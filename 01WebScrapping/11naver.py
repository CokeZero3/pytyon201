from selenium import webdriver
import time

url = ""

#드라이버 
driver = webdriver.Chrome("C:\\Python\\chromedriver.exe")
driver.get(url)

#더보기 클릭하기
while True:
    try:
        more = driver.find_element_by_css_selector('a.u_cbox_btn_more')
        more.click()
        time.sleep(2)
        