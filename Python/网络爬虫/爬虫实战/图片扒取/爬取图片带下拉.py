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
def getPicturesUrl(url_list, html, num):
    url_list = re.findall(r'\bhttp.*?.jpg\b',html)
    print('开始列举')
    pictures_url = []
    for i in url_list:
        if re.findall(r'\\',i):
            pass
        else:
            pictures_url.append(i)

    count = num*20
    print("正在保存")
    for url in pictures_url:
        # print("已保存" + str(round(((count+1)/len(pictures_url))*100)) + '%')
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
    num = 20
    for i in range(num):
        old_url = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=" + \
                  name + "&pn=" + str(i * 20)
        new_url = old_url + name
        html = getHTML(new_url)
        url_list = []
        getPicturesUrl(url_list, html, i)
main()
