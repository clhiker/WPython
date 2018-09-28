import requests
from bs4 import BeautifulSoup

# bs4默认编码是utf8

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
# print(soup)
print(soup.title)
print(soup.a)
print(soup.a.name)
print(soup.p.parent.name)
print(soup.html.contents)

