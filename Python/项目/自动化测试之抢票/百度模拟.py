#12306秒抢Python代码
from splinter.browser import Browser
from time import sleep

x = Browser(driver_name="chrome")
url = "https://kyfw.12306.cn/otn/index/initMy12306"
x = Browser(driver_name="chrome")
x.visit(url)

#
# x.fill("wd","李辉智障")
# x.find_by_id('su').click()

