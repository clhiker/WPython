from socket import *
import time

host = '10.6.113.170'
port = 8080
address = (host, port)

s = socket(AF_INET, SOCK_DGRAM)
s.bind(address)
print('Server is open')

while True:
    data, address = s.recvfrom(1024)
    print(data)


