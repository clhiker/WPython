import requests
import os

url = "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2824319473,2234748268&fm=27&gp=0.jpg"
url1 = "http://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=4108378450,811817369&fm=27&gp=0.jpg"
root = "D://pictures//"
path = root + url.split ('/')[-1]
try :
   if not os.path .exists (root):
      os.mkdir (root)
   if not os.path.exits(path):
      r = requests.get(url)
      with open(path, 'wb') as f:
         f.write(r.content )
         f.close()
         print("文件已经保存成功")
   else :
      print("文件已经存在")

except :
   print("爬取失败")

