from bypy import ByPy
from splinter.browser import Browser
from time import sleep

bp = ByPy()

x = Browser(driver_name='chrome')
url = "https://openapi.baidu.com/oauth/2.0/authorize?client_id=q8WE4EpCsau1oS0MplgMKNBn&response_type=code&redirect_uri=oob&scope=basic+netdisk"
x.visit(url)

username = '17615128161'
password = 'wykqh101119'
x.fill("userName",username)
x.fill('password',password)
x.click_link_by_id('TANGRAM_3__submit')

test = x.find_by_id('Verifier')

print(test)
print("\n")
bp.mkdir(remotepath='bypy')

bp.upload(localpath='d:\\ShareFile\2.jpg',remotepath='bypy',ondup='newcopy')

print('上传完毕！')