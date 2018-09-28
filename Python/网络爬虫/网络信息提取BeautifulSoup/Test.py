import requests
import re
from bs4 import BeautifulSoup

def getHTMLText(url):
    demo = requests.get("https://soulike.tech/").text
    soup = BeautifulSoup(demo, 'html.parser')
    print(soup.prettify())

def main():
    url0 = "https://soulike.tech"
    url1 = "https://soulike.tech/login"
    getHTMLText(url1)

main()



