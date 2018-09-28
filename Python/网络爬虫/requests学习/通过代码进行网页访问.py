import requests

try :
   url = "http://www.baidu.com/s"
   kv = {'wd':'Python'}
   r = requests.get (url, params = kv)
   print(r.request .url )
   r.raise_for_status ()
   r.encoding = r.apparent_encoding
   if(len(r.text)<100):
      print(len(r.text ))
   else :
      print(r.text[1000:2000])

except :
   print("访问出错")
