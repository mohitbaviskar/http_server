import threading
from socket import *
import sys
import os

portno = int(input())
serverName = '127.0.0.1'
def get_req(portno):
    clientsocket = socket(AF_INET, SOCK_STREAM)
    clientsocket.connect((serverName, portno))
    file = ['/index.html','/proxy/proxyfile.html','form.html']
    req = "GET /form.html HTTP/1.1\r\n" 
    req += "Accept: */*\r\n"
    req += "Host: 127.0.0.1:" + str(portno) + "\r\n"
    req += "Accept-Encoding: gzip, deflate, br\r\n"
    req += "Connection: keep-alive\r\n"
    req += "Cookie: yeXQbSuyXM=wdiXTApprS\r\n\r\n"
    clientsocket.send(req.encode())
    res = clientsocket.recv(1024).decode()
    print(res)

def head_req(portno):
    clientsocket = socket(AF_INET, SOCK_STREAM)
    clientsocket.connect((serverName, portno))
    file = ['/index.html','/proxy/proxyfile.html','form.html']
    req = "HEAD / HTTP/1.1\r\n" 
    req += "Accept: */*\r\n"
    req += "Host: 127.0.0.1:" + str(portno) + "\r\n"
    req += "Accept-Encoding: gzip, deflate, br\r\n"
    req += "Connection: keep-alive\r\n"
    req += "Cookie: yeXQbSuyXM=wdiXTApprS\r\n\r\n"
    clientsocket.send(req.encode())
    res = clientsocket.recv(1024).decode()
    print(res)

def post_req(portno):
    clientsocket = socket(AF_INET, SOCK_STREAM)
    clientsocket.connect((serverName, portno))
    req = "POST /posting.py HTTP/1.1\r\n"
    req += "Host: 127.0.0.1:" + str(portno) +"\r\n"
    req += "Connection: keep-alive\r\n"
    req += "Content-Length: \r\n"
    req += "Content-Type: application/x-www-form-urlencoded\r\n\r\n"
    req += "message= how are you, "
    clientsocket.send(req.encode())
    res = clientsocket.recv(1024).decode()
    print(res)


def put_req(portno):
    clientsocket = socket(AF_INET, SOCK_STREAM)
    clientsocket.connect((serverName, portno))
    req = "PUT /dir2/hello.txt HTTP/1.1\r\n"
    req += "Content-Type: text/plain\r\n"
    req += "Accept: */*\r\n"
    req += "Host: 127.0.0.1:15009\r\n"
    req += "Accept-Encoding: gzip, deflate, br\r\n"
    req += "Connection: keep-alive\r\n"
    req += "Content-Length: 10\r\n"
    req += "Cookie: CxmvKcxBpd=mnHjnHTAIN\r\n\r\n"
    req += "check test"
    clientsocket.send(req.encode())
    res = clientsocket.recv(1024).decode()
    print(res)

def del_req(portno):
    clientsocket = socket(AF_INET, SOCK_STREAM)
    clientsocket.connect((serverName, portno))
    req = "DELETE /dir2/hello.txt HTTP/1.1\r\n"
    req += "Content-Type: text/plain\r\n"
    req += "Accept: */*\r\n"
    req += "Host: 127.0.0.1:15009\r\n"
    req += "Accept-Encoding: gzip, deflate, br\r\n"
    req += "Connection: keep-alive\r\n"
    req += "Content-Length: 0\r\n"
    req += "Cookie: CxmvKcxBpd=mnHjnHTAIN\r\n\r\n"
    clientsocket.send(req.encode())
    res = clientsocket.recv(1024).decode()
    print(res)



for i in range(20):
    thread = threading.Thread(target=head_req,args=(portno,))
    thread.start()
    thread1 = threading.Thread(target=post_req,args=(portno,))
    thread1.start()
    thread2 = threading.Thread(target=get_req,args=(portno,))
    thread2.start()
    thread3 = threading.Thread(target=put_req,args=(portno,))
    thread3.start()
    thread4 = threading.Thread(target=del_req,args=(portno,))
    thread4.start()