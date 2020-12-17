import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

browser = webdriver.Chrome("C:\\Python\\chromedriver.exe")
browser.maximize_window() #창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)

# 가는 날 선택 + 클릭
browser.find_element_by_link_text("가는날 선택").click()
time.sleep(3)

#이번 달 27일, 28일 선택
# browser.find_element_by_link_text("18")[0].click() # [0] -> 이번달
# browser.find_element_by_link_text("19")[0].click() # [0] -> 이번달

#다음 달 27일, 28일 선택
# browser.find_element_by_link_text("28")[1].click() # [1] -> 다음달
# browser.find_element_by_link_text("29")[1].click() # [1] -> 다음달

# 이번 달, 다음 달 
browser.find_elements_by_link_text("18")[0].click() # [0] -> 이번달
browser.find_elements_by_link_text("29")[1].click() # [1] -> 다음달

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

#항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()
time.sleep(10)

try:
    #XPATH뿐 아니라 link_text, class_name 등 사용 가능
    ele = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # 성공했을 때 동작 수행
    print(ele.text) #첫번째 결과 출력
finally:
    browser.quit()
    #실패하면 끄기
    
# 결과 출력
# ele = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")

