from socket import *
from time import ctime

HOST = ' '
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print ("waiting for connection...")
    tcpSerSock, addr = tcpSerSock.accept()
    print ("...connection from:", addr)

    while True:
        data = tcpSerSock.recv(BUFSIZ)
        if not data:
            break
        tcpSerSock.send('[%s]%s' % (ctime(), data))

    tcpSerSock.close()
tcpSerSock.close()
