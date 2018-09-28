import os
import re
import urllib
import urllib2
import itertools
from string import maketrans

str_table = {
'_z2C$q': ':',
'_z&e3B': '.',
'AzdH3F': '/'
}

char_table = {
 'w': 'a',
 'k': 'b',
 'v': 'c',
 '1': 'd',
 'j': 'e',
 'u': 'f',
 '2': 'g',
 'i': 'h',
 't': 'i',
 '3': 'j',
 'h': 'k',
 's': 'l',
 '4': 'm',
 'g': 'n',
 '5': 'o',
 'r': 'p',
 'q': 'q',
 '6': 'r',
 'f': 's',
 'p': 't',
 '7': 'u',
 'e': 'v',
 'o': 'w',
 '8': '1',
 'd': '2',
 'n': '3',
 '9': '4',
 'c': '5',
 'm': '6',
 '0': '7',
 'b': '8',
 'l': '9',
 'a': '0'
 }

intab="wkv1ju2it3hs4g5rq6fp7eo8dn9cm0bla"
outtab="abcdefghijklmnopqrstuvw1234567890"
trantab = maketrans(intab, outtab)

char_table = {ord(key): ord(value) for key, value in char_table.items()}
def deCode(url):
    for key, value in str_table.items():
        url = url.replace(key, value)

    d=url.translate(trantab)
    return d

def getMoreURL(word):
  word = urllib.quote(word)
  url = r"http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E6%97%A0%E4%BA%BA%E6%9C%BA"
  urls = (url.format(word=word, pn=x) for x in itertools.count(start=0, step=30))
  return urls

def getHtml(url):
  page=urllib.urlopen(url)
  html=page.read()
  return html


def getImg(html):
  reg=r'"objURL":"(.*?)"'
  imgre=re.compile(reg)
  imageList=re.findall(imgre, html)
  imgUrls=[]

  for image in imageList:
      imgUrls.append(deCode(image))

  l=len(imgUrls)
  #print l
  return imgUrls

def downLoad(urls,path):
  global index
  for url in urls:
      print("Downloading:", url)
      res = urllib2.Request(url)
      try:
          response = urllib2.urlopen(res ,data=None, timeout=5)
      except urllib2.URLError, e:
         if hasattr(e,'code'):
             error_status = e.code
             print(error_status, "fail to download", url)
             continue
         elif hasattr(e,'reason'):
             print( "time out", url)
             continue

         continue

      #filename = os.path.join(path, str(index) + ".jpg")
      filename = "/home/python/pictures/"
      urllib.urlretrieve(url,filename)
      index += 1
      # urllib.urlretrieve(url[, filename[, reporthook[, data]]])

      if index-1==1000:
         break

if __name__ == '__main__':
    keyWord="表情包"
    index = 1
    #Savepath = "D:\TestDownload"
    Savepath = "D://picture"
    urls=getMoreURL(keyWord)

    for url in urls:
        downLoad(getImg(getHtml(url)),Savepath)
        if index-1==1000:
            break