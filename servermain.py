from socket import *
import sys
import os
import datetime

#default libraries 

import get_response from getting

#created files

server_socket = socket(AF_INET, SOCK_STREAM)
server_port = int(sys.argv[1])
server_socket.bind(('', server_port))
server_socket.listen(1)
print("server is on")


#server port assignment and listening to port



while True:
    connection_socket, addr = server_socket.accept()
    print('new request from')
    print(addr)
    print('connection_socket is')
    print(connection_socket)
    

    #connection to the client

    request = connection_socket.recv(1024).decode()
    response1 = request_checking(request)
    connection_socket.send(response1)


def request_checking(request):

    request_list = request.split()

    if(request_list[0] == 'GET'):
        response = get_response(request_list)
        return response
