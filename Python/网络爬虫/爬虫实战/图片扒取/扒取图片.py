import requests
import re
import sys

# 获取HTML信息
def getHTML(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("网页登录失败")
        return ""

# 获取图片的url
def getPicturesUrl(url_list, html):
    url_list = re.findall(r'\bhttp.*?.jpg\b',html)
    print('开始列举')
    pictures_url = []
    for i in url_list:
        if re.findall(r'\\',i):
            pass
        else:
            pictures_url.append(i)

    count = 0
    for url in pictures_url:
        sys.stdout.flush()
        print("已保存" + str(round(((count+1)/len(pictures_url))*100)) + '%')
        downLoadPictures(count, url)
        count += 1

#下载图片
def downLoadPictures(count, url):
    download_path = 'D://test/Picture/FirstTest/' + str(count) + '.jpg'
    try:
        r = requests.get(url)
        r.raise_for_status()
        with open(download_path, 'wb') as f:
            f.write(r.content)
            f.close()
    except:
        count-=1


def main():
    name = '无人机'
    old_url = "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word="

    new_url = old_url + name
    html = getHTML(new_url)
    url_list = []
    getPicturesUrl(url_list, html)

main()


#
# # url = "http://f10.baidu.com/it/u=866145389,1046219503&fm=72"
# url = "http://img4.imgtn.bdimg.com/it/u=3263750060,3582144846&fm=26&gp=0.jpg"
#
# path = "D://1.jpg"
# try :
#     r = requests.get(url)
#     with open(path, 'wb') as f:
#         f.write(r.content)
#         f.close()
#         print("文件已经保存成功")
#
# except :
#    print("爬取失败")

