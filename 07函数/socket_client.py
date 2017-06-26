# encoding=utf-8
# 是一个时间戳 TCP 客户端，它知道如何与 SocketServer 里 StreamRequestHandler 对象进行
# 通讯。
from socket import *

host = 'localhost'
port = 15000
bufsiz = 1024
addr = (host, port)

while True:
    tcpClientSock = socket(AF_INET, SOCK_STREAM)
    tcpClientSock.connect(addr)
    data = input('>')
    if not data:
        break
    tcpClientSock.send(('%s\r\n' % data).encode('utf-8'))
    #     我们可以用 readline()函数得到客户消息，用 write()函数把字
    # 符串发给客户。
    # 为了保持一致性，我们要在客户与服务器两端的代码里都加上回车与换行。实际上，你在代码
    # 中看不到这个，因为，我们重用了客户传过来的回车与换行。
    data = tcpClientSock.recv(bufsiz)
    if not data:
        break
    print(data.strip())

tcpClientSock.close()
