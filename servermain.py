from socket import *
import sys
import os
import datetime

#default libraries 

from getting import get_response
from heading import head_response
from posting import post_response

#created files

server_socket = socket(AF_INET, SOCK_STREAM)
server_port = int(sys.argv[1])
server_socket.bind(('', server_port))
server_socket.listen(1)
print("server is on")


#server port assignment and listening to port

def request_checking(request):
    req_list = request.split()
    if(req_list[0] == 'GET'):
        response = get_response(req_list)
        return response
    elif(req_list[0] == 'HEAD'):
        response = head_response(req_list)
        return response
    elif(req_list[0] == 'POST'):
        response = post_response(request)
        return response



while True:
    connection_socket, addr = server_socket.accept()
    print('new request from')
    print(addr)
    print('connection_socket is')
    print(connection_socket)
    

    #connection to the client
    while True:
        request = connection_socket.recv(1024).decode()
        print(request)
        response1 = request_checking(request)
        connection_socket.send(response1)
    # connection_socket.send(response1)
    connection_socket.close()



