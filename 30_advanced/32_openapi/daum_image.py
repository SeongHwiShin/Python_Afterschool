# open api 사용하기
# daum : http://developers.daum.net/
# bcca86e098f3a0820c8993017689c438

from urllib.request import urlopen, quote
import json
from pprint import pprint

apiKey = "2499a63929528241daff1ef20e2568e9"
q = "python"
output = "json"

url = "https://apis.daum.net/search/image?apikey={apiKey}&q={q}&output={output}" \
    .format(apiKey=apiKey, q=quote(q), output=output)

f = urlopen(url)

print(f.headers)
body = f.read()
print(body)
print(type(body))

# bytes -> str
s = body.decode("utf-8")
print(s)

# str -> dict
j = json.loads(s)
print(j)
print(type(j))

pprint(j)

# item['title'], item['image']
items = j['channel']['item']
print(items)

cnt = 1
for item in items:
    print("%d. title : %s, image : %s" % (cnt, item['title'], item['image']))
    cnt += 1

html = '''
<html>
<head>
<title>Daum Open API</title>
</head>
<body>
<h1>이미지 검색 결과</h1>
<ul>
'''
for item in items:
    html += '<li>'
    html += '<p>타이틀 : ' + item['title'] + '</p>'
    html += '<img src"' + item['image'] + '" width=200>'
    html += '<li>'

html += '''
</ul>
</body>
</html>
'''

with open('daum_image.html', 'w', encoding='utf-8') as f:
    f.write(html)
