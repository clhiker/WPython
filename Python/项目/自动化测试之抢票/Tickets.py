from splinter.browser import Browser
from time import sleep

username = u"cl1911618290"
passwd = u"wykqh101119"

starts = u"%u4E0A%u6D77%2CSHH"
ends = u"%u8425%u53E3%u4E1C%2CYGT"

dtime = u"2018-08-02"

order = 0

pa = u"陈乐"
ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"

login_url = "https://kyfw.12306.cn/otn/login/init"

#initmy_url = https://kyfw.12306.cn/otn/index/initMy12306

def login():
    b.find_by_text(u"登录").click()
    sleep(3)

login()