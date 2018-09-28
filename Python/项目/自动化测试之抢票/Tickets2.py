#12306秒抢Python代码
from splinter.browser import Browser

from selenium import webdriver

from time import sleep

x = Browser(driver_name="chrome")
url = "https://kyfw.12306.cn/otn/login/init"
x = Browser(driver_name="chrome")
x.visit(url)

#填写登陆账户、密码
x.fill("loginUserDTO.user_name","cl1911618290")
x.fill("userDTO.password","wykqh101119")
sleep(5)
x.find_by_id('loginSub').click()

# while True:
#     if(x.url != url):
#         break
#     else:
#         sleep(5)
#         x.find_by_id('loginSub').click()
#     sleep(1)
sleep(3)

x.visit("https://kyfw.12306.cn/otn/leftTicket/init")
#填写出发点目的地
x.cookies.add({"_jc_save_fromStation":"%u6DEE%u6EE8%2CHVN"})
x.cookies.add({"_jc_save_fromDate":"2018-09-02"})
x.cookies.add({u'_jc_save_toStation':'%u9526%u5DDE%2CJZD'})

#加载查询
while True:
    x.reload()
    x.find_by_text(u"查询").click()
    # 预定
    x.find_by_text(u"预订")[1].click()
    sleep(3)
    if (x.url == "https://kyfw.12306.cn/otn/confirmPassenger/initDc"):
        break


#选择乘客
x.find_by_text(u"陈乐(学生)")[0].click()
#选择硬卧
x.find_by_id("seatType_1").click()

#确认学生票
x.find_by_id("dialog_xsertcj_ok").click()

#提交订单
x.find_by_id("submitOrder_id").click()

