import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window() #避免移动版布局和网页版布局窗口影响CSS定位抓取
#此处,可以设置查找元素时超时问题,异常检测driver.implicity_wait(5),超过5秒报异常

###为了防止等待抓取超时报错,可以类似的设置打开页面异常检测,这里直接忽略异常继续往下抓取,页面上重要元素几乎都拿到了###
try:
    driver.get('http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=无人机')
except:
    pass

elements=[] #为了判断是否页面下拉完毕,显示了全部页面元素
count=-1
###while语句条件,下拉刷新判断关键条件,可以参照页面html源码对照看有多少个元素a###
while len(elements) > count:
    count = len(elements) #记录当前找到多少元素
    driver.execute_script('window.scrollBy(0, document.body.scrollHeight);') #找到元素后,做页面下拉刷新
    #execute_script利用javascript模拟动态网页页面下拉,scrollBy参数是0表示从0开始下拉,可以修改成任意高度
    time.sleep(2)
    elements=driver.find_elements_by_css_selector('div.products-list > div > a')
    #元素a定位,find_elements_by_css_selector里elements表示找所有满足条件的元素,element表示找一个满足条件的元素
for element in elements:
    ###此处可以嵌套查找elements里的元素element.find_XXX_by_css_selector(元素)###
    print(element.get_attribute('href'))
    #selenium里的get_attribute类似bs4里的get
driver.quit()