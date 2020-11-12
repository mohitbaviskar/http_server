import datetime
from resource import *
import os.path
from socket import *
# root = "./documentroot"
from configparser import ConfigParser

parser = ConfigParser()
parser.read('server.conf')



root = parser.get('documentroot','documentroot')
ipadd = parser.get('HOST', 'host')


form_complete = "./documentroot/form.html"
#request = input()

def post_response(request):
    r = request.split('\r\n')
    req_list = request.split()
    post_list = request.split('\r\n\r\n')
    print(post_list)

    postlog = req_list[0] + " " + req_list[1] + " " + req_list[2] + " "




    # if('Content-Length' in req_list):
    #     i = req_list.index('Content-Length')
    #     j = req_list[i].split(':')
    #     input += j[1] + " "
    # else:
    #     input += "- "

    postlog += post_list[1]
    postlog += " \n"
    
    

    file_name = form_complete
    status_code_det = "200"

    response = "HTTP/1.1 "+ status_code_det + " " + status_dict[status_code_det] + "\r\n"
    response += get_date()
    response += "Server: Mohit's server/0.0.1 (Ubuntu)\r\n"
    #print(file_name)



    last_modified = os.path.getmtime(file_name)
    response += ("last-Modified: " + datetime.datetime.fromtimestamp(last_modified).strftime("%a, %d %b, %Y %I:%M:%S")+ " GMT\r\n")
    



    mime_type = get_mime_type(file_name)
    read_type = mime_type.split('/')[0]



    if(read_type == 'text'):
        file_pointer = open(file_name)
        body = file_pointer.read()
        body = body.encode()
    
    # if(mime_type == 'None'):
    #     body = b""
    #     with open(file_name, "rb") as file_pointer:
    #         byte = file_pointer.read(1)
    #         while byte != b"":
    #             # Do stuff with byte.
    #             body += byte
    #             byte = file_pointer.read(1)



            
    length = len(body)

    response += "Content-Type: " + mime_type + "\r\n"
    response += "Content-Length: " + str(length) + "\r\n"

    response += "Connection: close\r\n\r\n"

    accesslog = ipadd + " " + "-" + " "
    accesslog += "-" + " "
    x = datetime.datetime.now()
    accesslog += "[" + x.strftime("%d/%b/%Y:%X +0530") + "]" + " "
    accesslog += "\"" + r[0] + "\"" + " " 
    accesslog += status_code_det + " "
    accesslog += str(length) + " " +"\n"
    f = open('log/access.log','a')
    f.write(accesslog)
    file_insert = open('log/post.log','a')
    file_insert.write(postlog)

    error = ["400","401","405","404","407","406"]
    if status_code_det in error:
        errorlog = x.strftime("[%a %b %d %X.%f %Y]")
        errorlog += " " + "[error]" + " "
        errorlog += "[" +"pid" + str(os.getpid()) + "]" + " "
        errorlog += "[client " +ipadd + "]" + " "
        errorlog += status_dict[status_code_det] + "\n"
        f = open('log/error.log','a')
        f.write(errorlog)

    response = response.encode()
    response_enc = response + body



    # print(response_enc)
    return response_enc

#post_response(request)