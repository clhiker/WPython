# from splinter.browser import Browser
# from time import sleep
# import traceback
#
# # 设定用户名，密码
# username = u"cl1911618290"
# passwd = u"wykqh101119"
#
# # 起始地址的cookies值要自己去找, 下面两个分别是上海, 营口东。如何找，我们在文#后有简单的介绍
#
# starts = u"%u6DEE%u6EE8%2CHVN"
#
# ends = u"%u9526%u5DDE%2CJZD"
#
# # 时间格式
#
# dtime = u"2018-09-01"
#
# # 车次，选择第几趟，0则从上之下依次点击
#
# order = 1
#
# #设定乘客姓名
#
# pa = u"陈乐"
#
# #设定网址
#
# ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
#
# login_url = "https://kyfw.12306.cn/otn/login/init"
#
# initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"
#
# #登录网站
#
# def login():
#
#     b.find_by_text(u"登录").click()
#
#     sleep(3)
#
#     #我们在这里尝试了模拟登录12306，得到结果如下：
#
#
#
#     #第17至20行代码用于自动登录，username是12306账号名，passwd是12306密码
#
#     b.fill("loginUserDTO.user_name", username)
#
#     sleep(1)
#
#     b.fill("userDTO.password", passwd)
#
#     sleep(1)
#
#     #在我们的模拟登录中，结果如下：
#
#     #接下来的验证码还是要大家自己动手输入啦！据说12306的验证码辨识难度堪比常识竞赛。在此，大数据文摘祝你好运！
#
#     print(u"等待验证码，自行输入...")
#
#     while True:
#         if b.url != initmy_url:
#             sleep(1)
#         else:
#             break
#
#     #购票
#
# def huoche():
#
#     global b
#     #使用splinter打开chrome浏览器
#     b = Browser(driver_name="chrome")
#
#     #返回购票页面
#
#     b.visit(ticket_url)
#
#     #现在让我们来看看程序运行结果
#
#
#     # huoche()
#
#
#
#     # 看到了吗？网页能正常打开！
#
#     while b.is_text_present(u"登录"):
#
#         sleep(1)
#
#         login()
#
#         if b.url == initmy_url:
#             break
#
# try:
#
#     print u"购票页面..."
#
#     # 跳回购票页面
#
#     b.visit(ticket_url)
#     # 加载查询信息
#
#     # 我们的模拟登录中以上海为始发站，营口东为终点站，时间选定2016年2月1日
#
#     b.cookies.add({"_jc_save_fromStation": starts})
#
#     b.cookies.add({"_jc_save_toStation": ends})
#
#     b.cookies.add({"_jc_save_fromDate": dtime})
#
#     b.reload()
#
# #让我们一起来看看运行结果如何？
#
#
#
#        sleep(2)
#
#        count = 0
#
#        # 循环点击预订
#
#        if order != 0:
#
#            while b.url == ticket_url:
#
#                b.find_by_text(u"查询").click()
#
# #程序自动点击查询后，结果如下：
#
#
#
#                count +=1
#
#                print u"循环点击查询... 第 %s 次" % count
#
#                sleep(1)
#
#                try:
#
#                    b.find_by_text(u"预订")[order - 1].click()
#
# 程序自动点击预订后，结果如下：
#
#
#
# 哇啦！我们成功预订了春运车票！
#
# 56                except:
#
# 57                    print u"还没开始预订"
#
# 58                    continue
#
# 59        else:
#
# 60            while b.url == ticket_url:
#
# 61                b.find_by_text(u"查询").click()
#
# 62                count += 1
#
# 63                print u"循环点击查询... 第 %s 次" % count
#
# 64                sleep(1)
#
# 65                try:
#
# 66                    for i in b.find_by_text(u"预订"):
#
# 67                        i.click()
#
# 68                except:
#
# 69                    print u"还没开始预订"
#
# 70                    continue
#
# 71        sleep(1)
#
# 注意：可以通过修改sleep的参数来调整延时, 但延时不要太低, 防止被12306网站认为是刷票屏蔽掉.
#
# 72        b.find_by_text(pa)[1].click()
#
# 如果你运气不好，程序会给出一个这样的信息：
#
# 73        print  u"能做的都做了.....不再对浏览器进行任何操作"
#
# 如果出现这样的信息，你也不要灰心，重新执行程序，让好运降临！
#
# 74    except Exception as e:
#
# 75        print(traceback.print_exc())
#
# 76 if __name__ == "__main__":
#
# 77     huoche()