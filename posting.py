import datetime
from resource import *
import os.path
from socket import *
root = "./cakesite"


#request = input()

def post_response(request):
    req_list = request.split()
    post_list = request.split('\r\n\r\n')
    print(post_list)
    data_page = root + req_list[1]

    input = req_list[0] + " " + req_list[1] + " " + req_list[2] + " "




    # if('Content-Length' in req_list):
    #     i = req_list.index('Content-Length')
    #     j = req_list[i].split(':')
    #     input += j[1] + " "
    # else:
    #     input += "- "

    input += post_list[1]
    input += " \n"
    
    file_insert = open("post_log.txt","a")
    file_insert.write(input)

    path_to_check = root + req_list[1]
    if(os.path.isfile(path_to_check)):
        file_name = path_to_check
        status_code_det = "200"
    else:
        status_code_det = "404"

    response = "HTTP/1.1 "+ status_code_det + " " + status_dict[status_code_det] + "\n"
    cur_time = datetime.datetime.now()
    response += ("Date: " + cur_time.strftime("%A") + ", "+ cur_time.strftime("%d") + " " +  cur_time.strftime("%b") + " " + cur_time.strftime("%Y") + " " + cur_time.strftime("%X") + " GMT\n")
    response += "Server: Mohit's server/0.0.1 (Ubuntu)\n"
    #print(file_name)



    last_modified = os.path.getmtime("httpserver.py")
    response += ("last-Modified: " + datetime.datetime.fromtimestamp(last_modified).strftime("%A, %d %b, %Y %I:%M:%S")+ " GMT\n")
    



    mime_type = get_mime_type(file_name)
    read_type = mime_type.split('/')[0]



    if(read_type == 'text'):
        file_pointer = open(file_name)
        body = file_pointer.read()
        body = body.encode()
    
    if(mime_type == 'None'):
        body = b""
        with open(file_name, "rb") as file_pointer:
            byte = file_pointer.read(1)
            while byte != b"":
                # Do stuff with byte.
                body += byte
                byte = file_pointer.read(1)



            
    length = len(body)

    response += "Content-Type: " + mime_type + "\n"
    response += "Content-Length: " + str(length) + "\n"

    response += "Connection: keep-alive\n\n"
    response = response.encode()
    response_enc = response + body



    # print(response_enc)
    return response_enc

#post_response(request)