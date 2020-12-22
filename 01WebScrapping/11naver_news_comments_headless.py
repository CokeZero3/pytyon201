from selenium import webdriver
import time
import pandas as pd
import os


url = 'https://news.naver.com/main/ranking/read.nhn?m_view=1&includeAllCount=true&mode=LSD&mid=shm&sid1=001&oid=023&aid=0003580116&rankingType=RANKING'

#웹 드라이버
driver = webdriver.Chrome('C:\\Python\\chromedriver.exe')
driver.implicitly_wait(15)
driver.get(url)

#더보기 계속 클릭하기
while True:
    try:
        더보기 = driver.find_element_by_css_selector('a.u_cbox_btn_more')
        더보기.click()
        time.sleep(1)
    except:
        break

str_comments= []

#댓글추출
contents = driver.find_elements_by_css_selector('span.u_cbox_contents')
for content in contents:
    print(content.text)

for i in range(len(contents)):
       str_tmp = str(contents[i].text)
       str_tmp = str_tmp.replace('\n', '') 
       str_tmp = str_tmp.replace('\t', '') 
       str_tmp = str_tmp.replace('      ','') 
       str_comments.append(str_tmp)  

df = {"댓글":str_comments}
naver_pd = pd.DataFrame(df)

print(naver_pd)

#csv 저장
if not os.path.exists('C:\\Python\\01Crawling\\01naver\\naver_tsv\\test2.tsv'):
    naver_pd.to_csv('C:\\Python\\01Crawling\\01naver\\naver_tsv\\test2.tsv', sep='\t', index=True, mode='w', encoding='utf-8-sig', header=None)
else:
    naver_pd.to_csv('C:\\Python\\01Crawling\\01naver\\naver_tsv\\test2.tsv', sep='\t', index=True, mode='a', encoding='utf-8-sig', header=None)
