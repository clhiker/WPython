from socket import *
s = socket(AF_INET, SOCK_STREAM)

port = 80 #socket.getserbbyname('http', 'tcp')
# ip = 192.168.1.12
address = ('www.baidu.com', 8080)
s.connect(address)
print('down')


