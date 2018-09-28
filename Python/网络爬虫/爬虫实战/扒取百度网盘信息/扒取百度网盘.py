import requests

try:
    r = requests.get('https://pan.baidu.com/')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("扒取失败")
# print(requests.get('https://pan.baidu.com/').text)