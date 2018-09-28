from socket import *
import time

host = '10.6.113.170'
port = 8080
address = (host, port)

# 两个参数分别是指定IPv4协议以及指定UDP发送方式
s = socket(AF_INET, SOCK_DGRAM)
s.connect(address)

while True:
    message = input('send message')
    s.sendto(message.encode('utf-8'), address)
    data = s.recv(1024)
    print(data)
    time.sleep(0.001)
