from socket import *
import sys
import os.path
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = int(sys.argv[1])
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("server is running")
while True:
    connectionSocket, addr = serverSocket.accept()
    print('new request received from ')
    print(addr)
    print('connectionSocket is ')
    print(connectionSocket)
    sentence = connectionSocket.recv(1024).decode()
    words = sentence.split()
    print(words[0],words[1])
    if(words[0] == 'GET'):
        string = "HTTP/1.1 200 OK\n"
        string += "DATE: Wed, 30 Sep 2020 09:35:34 GMT\n"
        string += "Server: Mohit's server/0.0.1 (Ubuntu)\n"
        string += "Content-Length:72\n"
        string += "Connection: close\n"
        string += "Content-Type: text/html; charset=iso-8859-1\n\n"
        
    connectionSocket.close()