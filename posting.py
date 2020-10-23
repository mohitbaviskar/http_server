import datetime
from resource import *
import os.path
from socket import *
root = "./documentroot"

form_complete = "/form.html"
#request = input()
data_page = "documentroot/server_data/post_log.txt"

def post_response(request):
    req_list = request.split()
    post_list = request.split('\r\n\r\n')
    print(post_list)

    input = req_list[0] + " " + req_list[1] + " " + req_list[2] + " "




    # if('Content-Length' in req_list):
    #     i = req_list.index('Content-Length')
    #     j = req_list[i].split(':')
    #     input += j[1] + " "
    # else:
    #     input += "- "

    input += post_list[1]
    input += " \n"
    
    file_insert = open(data_page,"a")
    file_insert.write(input)

    path_to_check = root + form_complete
    if(os.path.isfile(path_to_check)):
        file_name = path_to_check
        status_code_det = "200"
    else:
        status_code_det = "404"

    response = "HTTP/1.1 "+ status_code_det + " " + status_dict[status_code_det] + "\r\n"
    response += get_date()
    response += "Server: Mohit's server/0.0.1 (Ubuntu)\r\n"
    #print(file_name)



    last_modified = os.path.getmtime(file_name)
    response += ("last-Modified: " + datetime.datetime.fromtimestamp(last_modified).strftime("%A, %d %b, %Y %I:%M:%S")+ " GMT\r\n")
    



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

    response += "Content-Type: " + mime_type + "\r\n"
    response += "Content-Length: " + str(length) + "\r\n"

    response += "Connection: close\r\n\r\n"
    response = response.encode()
    response_enc = response + body



    # print(response_enc)
    return response_enc

#post_response(request)