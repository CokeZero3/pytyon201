# Python 샘플 코드 #

from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import requests, bs4
import pandas as pd
from lxml import html


url = 'http://apis.data.go.kr/B551182/diseaseInfoService/getDissByGenderAgeStats'
myApiKey = unquote('YCUlhSY8FaicJZ7J1Gq6t0036q3XEwV8susgVh4FnI9FyAjxOX0FlYWaFoHsKF1zCEQnJ%2Fo7HKuUsztp%2FJmh8A%3D%3D')
queryParams = '?' + urlencode(
    { 
     quote_plus('ServiceKey') : myApiKey, 
     quote_plus('year') : '2014', 
     quote_plus('sickCd') : 'J00', 
     quote_plus('sickType') : '1', 
     quote_plus('medTp') : '2' 
     }
 )

response = requests.get(url+queryParams).text.encode('utf-8')
xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')
# xmlobj    # 디버깅용.

rows = xmlobj.findAll('item')
# print(rows)
# print(rows[0])

# rows    # 디버깅용.
columns = rows[0].find_all()
# print(columns)
# columns    # 디버깅용.
# print(columns[1].name)    # 디버깅용.
# print(columns[1].text)    # 디버깅용.

# 모든 행과 열의 값을 모아 매트릭스로 만들어보자.
rowList = []
nameList = []
columnList = []

rowsLen = len(rows)
for i in range(0, rowsLen):
    columns = rows[i].find_all()
    
    columnsLen = len(columns)
    for j in range(0, columnsLen):
        # 첫 번째 행 데이터 값 수집 시에만 컬럼 값을 저장한다. (어차피 rows[0], rows[1], ... 모두 컬럼헤더는 동일한 값을 가지기 때문에 매번 반복할 필요가 없다.)
        if i == 0:
            nameList.append(columns[j].name)
            print("nameList:", nameList)
        # 컬럼값은 모든 행의 값을 저장해야한다.    
        eachColumn = columns[j].text
        columnList.append(eachColumn)
        print("columnList: ", columnList)

    rowList.append(columnList)
    print(rowList)
    columnList = []    # 다음 row의 값을 넣기 위해 비워준다. (매우 중요!!)
    
# result = pd.DataFrame(rowList, columns=nameList)
# result.head()