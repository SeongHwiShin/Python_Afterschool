# https://developers.skplanetx.com/my-center/app-station/
# 270bf4cf-ff38-3c9e-9d55-2add22f156f0
from urllib.request import urlopen, Request
import json

apiKey = "270bf4cf-ff38-3c9e-9d55-2add22f156f0"
page = "1"
count = "10"

url = "http://apis.skplanetx.com/melon/charts/realtime?version={version}&page={page}&count={count}"\
    .format(version = 1, page = page, count = count)

req = Request(url)
req.add_header('appKey', apiKey)

f = urlopen(req)

print(f.headers)

body = f.read()
print(body)

