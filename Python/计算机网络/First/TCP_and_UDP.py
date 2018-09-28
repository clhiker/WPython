from socket import *
#import socket

def test_UDP():
    serverName = '119.75.216.20'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = input("Input lowercase sentence:")
    clientSocket.sendto(message.encode(),(serverName,serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage)
    clientSocket.close()

def UDP():
    s = socket(AF_INET, SOCK_STREAM)
    return s

def DNS_changeto_IP():
    remote_ip = gethostbyname('www.baidu.com')
    print(remote_ip)
    port = 80
    s = UDP()
    s.connect((remote_ip,port))     #ip+port
    message = "hhda"
    s.sendall(message.encode('utf-8'))
    relay = s.recv(4096)
    print(relay)
    s.close()


def main():
    DNS_changeto_IP()
    #test_UDP()

if __name__ == '__main__':
    main()
