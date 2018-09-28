from splinter.browser import Browser
import time


x = Browser(driver_name='chrome')
url = 'https://pan.baidu.com/'
x.visit(url)

time.sleep(20)

x.visit('https://pan.baidu.com/disk/home?errno=0&errmsg=Auth%20Login%20Sucess&&bduss=&ssnerror=0&traceid=#/all?path=%2F&vmode=list')

# x.click_link_by_id('TANGRAM__PSP_4__footerULoginBtn')
#
# username = '17615128161'
# password = 'wykqh101119'
# x.fill("userName",username)
# x.fill('password',password)
# x.click_link_by_id('TANGRAM__PSP_4__submit')
#
# test = x.find_by_id('Verifier')
#
# print(test)
# print("\n")
#
# print('上传完毕！')