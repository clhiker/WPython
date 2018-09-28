import json
import requests

data = input("请输入翻译内容")
data = data
url = "http://fanyi.baidu.com/basetrans"

data = {
    "query": data,
    "from": 'zh',
    "to": 'jp',
}

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36",
}

response = requests.post(url, data=data, headers=headers)
dir = response.content.decode('unicode-escape')
begin = int(dir.find(r'"dst":'))
end = int(dir.find(r'"prefixWrap"'))
result = dir[begin + 7:end - 2]
print(result)


