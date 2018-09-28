#coding:utf-8
#__author__：MagicWang
from selenium import webdriver
import time
import re
import requests

global i
i = 0




keywords="drone+flying+picture"
driver = webdriver.Firefox()
driver.get("https://www.google.com/search?biw=629&bih=599&tbm=isch&sa=1&q="+keywords)
js="var q=document.documentElement.scrollTop=200000"
driver.execute_script(js)
driver.implicitly_wait(5)
"""elements = driver.find_elements_by_class_name('smb')
for element in elements:
    element.click()"""
content=driver.page_source.encode("utf-8")
x=0
number = 0
for page_num in range(10):
    waitCount = 0
    print('page:'+str(page_num+1))
    driver.execute_script(js)
    while(content==driver.page_source.encode("utf-8")):
        waitCount += 1
        time.sleep(0.2)
        print ("waitCount:" + str(waitCount))
        if(waitCount >= 20):
            break
    if(waitCount >= 20):
        break
    print ("new content")
    content = driver.page_source.encode("utf-8")
elements = driver.find_element_by_id('smb')
elements.click()
time.sleep(1)
content = driver.page_source.encode("utf-8")

for page_num in range(10):
    waitCount = 0
    print('page:'+str(page_num+1))
    driver.execute_script(js)
    while(content==driver.page_source.encode("utf-8")):
        waitCount += 1
        time.sleep(0.2)
        print ("waitCount:" + str(waitCount))
        if(waitCount >= 20):
            break
    if(waitCount >= 20):
        break
    print ("new content")
    content = driver.page_source.encode("utf-8")

original=r'"ou":"(.*?)"'
address=re.findall(original,str(content))
for link in set(address):
    print(link)
    x+=1
    print(x)
    try:
        pic = requests.get(link,timeout=10)
    except requests.exceptions.ConnectionError:
            print 'error: the picture cannot be downloaded'
            continue
    except requests.exceptions.ReadTimeout:
            print 'error:Timeout! the website cannot be visited'
            continue
    string = 'F:\\drone_flying_picture\\'+str(i) + '.jpg'
    #resolve the problem of encode, make sure that chinese name could be store
    fp = open(string.decode('utf-8').encode('cp936'),'wb')
    fp.write(pic.content)
    fp.close()
    i = i + 1