from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome() #("C:/Python/chromedriver.exe")
browser.get("http://naver.com")

"""[셀레니움 기본 사용법]: Terminal에서 사용하는 법
>>> from selenium import webdriver
>>> browser = webdriver.Chrome()
>>> browser.get("http://naver.com") 

#네이버 로그인 버튼 클릭하기
>>> ele = browser.find_element_by_class_name("link_login") 
>>> ele.click()  

>>> browser.back()
>>> browser.forward()
>>> browser.refresh()

#네이버에서 검색창 커서
>>> ele = browser.find_element_by_id("query") 
#엔터치기
>>> from selenium.webdriver.common.keys import Keys #엔터 치려면 임포트 Keys 해야함
>>> ele.send_keys(Keys.ENTER)

#
>>> ele = browser.find_element_by_tag_name("a")
>>> ele
>>> ele = browser.find_elements_by_tag_name("a") 
>>> ele

#
>>> for e in ele:             f")
...     e.get_attribute("href")     
... 

#다음으로 이동
>>> browser.get("http://daum.net")
>>> ele = browser.find_element_by_name("q")
>>> ele

#xpath 
ele = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")                                               et/div/div/button[2]") 
>>> ele.click()
"""