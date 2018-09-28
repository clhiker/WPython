import requests
url = "https://www.amazon.cn/悲观主义的花朵-廖一梅/dp/B074X87MW6/ref=tmm_kin_swatch_0?_encoding=UTF8&qid=&sr="
try :
   kv = {'user-agent':'Mozilla/5.0'}
   r = requests.get(url, headers = kv)
   r.raise_for_status ()
   r.encoding = r.apparent_encoding
   print(r.text[1000:2000])
except :
   print("爬取失败")
