##通用代码框架

import requests

def getHTMLText(url):
   try:
      r = requests.get(url,timeout = 30)
      r = raise_for_status()     #当返回值不是200时将转到except并抛出
      r.encoding = r.apparent_encoding
      return r.text
   except:
      return "产生异常"

if __name__ == "__main__":
   url = "//www.baidu.com"
   print(getHTMLText)
   print("智障")
