import requests
from bs4 import BeautifulSoup
import bs4

# 获取HTML
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "连接超时"

# 将HTML标签存入数据结构中
def finUnivList(ulist, html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,
                          tds[1].string,
                          tds[3].string])

# 标准化输出结果
def printUnivList(ulist, num):
    print("Suc" + str(num))
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format(
        "排名","学校名称","总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(
            u[0], u[1], u[2],chr(12288)))


def main():
    num = int(input("请输入排名"))
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    finUnivList(uinfo, html)
    printUnivList(uinfo, num)

main()