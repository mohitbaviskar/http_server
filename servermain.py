from socket import *
import sys
import os
import datetime

#default libraries 

from getting import get_response

#created files

server_socket = socket(AF_INET, SOCK_STREAM)
server_port = int(sys.argv[1])
server_socket.bind(('', server_port))
server_socket.listen(1)
print("server is on")


#server port assignment and listening to port

def request_checking(req_list):
    if(req_list[0] == 'GET'):
        response = get_response(req_list)
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
        # print(request)
        req_list = request.split()
        response1 = request_checking(req_list)
        print(response1)
        connection_socket.send(response1)
    # connection_socket.send(response1)
    connection_socket.close()



