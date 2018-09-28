from selenium import webdriver

drive = webdriver.Chrome()
url = 'https://soulike.tech/login'
drive.get(url)
for i in range(100):
    drive.find_element_by_name('登录').click()
