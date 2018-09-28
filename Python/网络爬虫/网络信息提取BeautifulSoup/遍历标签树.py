import requests
from bs4 import BeautifulSoup

demo = requests.get("http://python123.io/ws/demo.html").text
soup = BeautifulSoup(demo,'html.parser')

# 下行遍历
# 遍历儿子节点
for child in soup.body.contents:
    print(child)
# 遍历子孙节点
for child in soup.body.children:
    print(child)

# 上行遍历
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

# 平行遍历
# 遍历后续节点
for sibling in soup.a.next_siblings:
    print(sibling)
# 遍历前续节点
for sibling in soup.a.previous_siblings:
    print(sibling)