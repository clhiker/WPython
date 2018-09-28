from bs4 import BeautifulSoup
import requests
demo = requests.get("http://python123.io/ws/demo.html").text
soup = BeautifulSoup(demo,'html.parser')

# 将每一个标签后面加了一个换行符
print(soup.prettify())