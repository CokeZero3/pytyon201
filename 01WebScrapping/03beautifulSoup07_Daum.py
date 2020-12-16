import requests
from bs4 import BeautifulSoup



for year in range(2015, 2021):
    print("Year: ", year)
    url = "https://search.daum.net/search?w=tot&m=&q={}%EB%85%84%20%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&nzq=%EC%98%81%ED%99%94%202019%EB%85%84&DA=NSJ".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})
    
    for idx, image in enumerate(images):
        # print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
            
        print(image_url)
        
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        
        
        #사진 저장
        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)
            
        if idx >= 4: #상위 5개 까지만 다운로드
            break