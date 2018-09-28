import requests

try :
   url = "http://m.ip138.com/ip.asp?ip="
   r = requests.get(url + "210.30.96.83")
   r.raise_for_status()
   print(r.text)

except :
   print("获取失败")
   
