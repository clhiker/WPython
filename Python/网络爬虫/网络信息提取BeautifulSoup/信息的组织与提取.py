# 信息标记语言
# XML JSON YAML

# 信息提取
import re
import requests
from bs4 import BeautifulSoup

demo = requests.get("http://python123.io/ws/demo.html").text
soup = BeautifulSoup(demo,'html.parser')

for link in soup.find_all(['a','b']):
    print(link)

# 查找所以链接
for link in soup.find_all('a'):
    print(link.get('href'))

# 返回所以标签
for tag in soup.find_all(True):
    print(tag.name)

# 返回以B开头的所有标签名字
for tag in soup.find_all(re.compile('b')):
    print(tag.name)
# 第二个参数属性
print(soup.find_all(id='link1'))
print(soup.find_all(id=re.compile('link')))

# 第三个参数是否显示子标签
print(soup.find_all(recursive=True))
print(soup.find_all(recursive=False))
# 第三个参数查看字符串
print(soup.find_all(string = 'python'))
print(soup.find_all(string = re.compile('python')))

# find_all简写
print(soup(string='python'))