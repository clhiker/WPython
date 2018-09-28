#
# date : 2018年9月6日
# IDE : Pycharm
# Author : 陈乐
# note : 实现对图片的大规模的不精确的扒取
#
import re
import requests
import configparser

class PickUpPictures:
    def __init__(self):
        self.origin_url = ""
        self.html = ""
        self.picture_name = 0
        self.limit_number = 0

        # 满足开闭原则，获取存储路径
        cf = configparser.ConfigParser()
        cf.read('config.ini')
        self.path_name = cf.get('Path','name')

    def getHTML(self):
        try:
            r = requests.get(self.origin_url)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            self.html = r.text
        except:
            print("网页登录失败")

    def getPictureUrl(self):
        # 正则获取所有图片网址
        url_list = re.findall(r'\bhttp.*?.jpg\b', self.html)
        # 去除重复
        unique_url_list = list(set(url_list))

        # 获取可用的图片地址
        for url in unique_url_list:
            if re.findall(r'\\', url):
                pass
            else:
                self.downLoadPicture(url)
            # 限制下载数量
            if self.picture_name >= self.limit_number:
                break


    def downLoadPicture(self, url):
        # 获取实际存储路径
        download_path = self.path_name + str(self.picture_name) + '.jpg'

        try:
            r = requests.get(url,timeout=3)
            r.raise_for_status()
            # 开始存储图片
            with open(download_path, 'wb') as f:
                f.write(r.content)
                f.close()
            self.picture_name += 1
            print('已成功扒取' + str(self.picture_name) + "张")
        except:
            pass

    def control(self):
        pick_name = input('请输入要扒取的图片名称')
        pick_number = input('请输入要扒取的数量')

        self.limit_number = int(pick_number)
        # 对下载数量的模糊控制（所以这是不定向下载）
        page_number = int(pick_number)//20

        for counter in range(page_number + 1):
            self.origin_url = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=" + \
                      pick_name + "&pn=" + str(counter * 20)
            self.getHTML()
            self.getPictureUrl()
            if self.picture_name >= self.limit_number:
                break


if __name__ == '__main__':
    pickup_pictures = PickUpPictures()
    pickup_pictures.control()