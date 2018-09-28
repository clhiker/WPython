# ##通用代码框架
#
# import requests
#
# def getHTMLText(url):
#    try:
#       r = requests.get(url,timeout = 30)
#       r = raise_for_status()     #当返回值不是200时将转到except并抛出
#       r.encoding = r.apparent_encoding
#       #return r.text
#    except:
#       return "产生异常"
#
# if __name__ == "__main__":
#    url = "www.baidu.com"
#    print(getHTMLText)
#    print("智障")
import urllib.request
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/49.0.2')]
file = "https://www.baidu.com"
try:
    opener.open(file)
    print('No problem')
except urllib.request.HTTPError:
    print("Can't open")
except urllib.request.URLError:
    print("Can't open")