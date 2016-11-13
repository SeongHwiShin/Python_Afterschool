
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://comic.naver.com/index.html')
soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())

ol = soup.find('ol', {'id': 'realTimeRankFavorite'})
items = ol.find_all('a')
print(items)

rank = 1
for item in items:
    print("%d, %s" % (rank, item.text))
    rank += 1

# 반복 수행하기
while(True):
    66naver_webtoon()
    time.sleep(1)