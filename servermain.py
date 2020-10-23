from socket import *
import sys
import os
import datetime
import threading
#default libraries 

from getting import get_response
from heading import head_response
from posting import post_response
from putting import put_response
from deleting import delete_response

#created files

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_port = int(sys.argv[1])
server_socket.bind(('', server_port))
server_socket.listen(1)
print("server is on")


#server port assignment and listening to port

def request_handler(connection_socket):
    try:
        request = connection_socket.recv(1024).decode('utf-8')
        while True:
            if(request == ""):
                connection_socket.close()
                break
            else:
                req_list = request.split()
                if(req_list[0] == 'GET'):
                    response = get_response(req_list)
                elif(req_list[0] == 'HEAD'):
                    response = head_response(req_list)
                elif(req_list[0] == 'POST'):
                    response = post_response(request)
                elif(req_list[0] == 'PUT'):
                    response = put_response(request)
                elif(req_list[0] == 'DELETE'):
                    response = delete_response(req_list)
            connection_socket.send(response)
            connection_socket.close()
            break
    except OSError:
        print("client disconnected")
    




while True:
    connection_socket, addr = server_socket.accept()
    print('new request from')
    print(addr)
    print('connection_socket is')
    print(connection_socket)
    request_handler(connection_socket)
    thread = threading.Thread(target=request_handler,args=[connection_socket,])
    thread.start()
    # #connection to the client
    # while True:
    #     request = connection_socket.recv(1024).decode()
    #     print(request)
    #     response1 = request_checking(request)
    #     print(response1)
    #     connection_socket.send(response1)
    # # connection_socket.send(response1)
    # connection_socket.close()



