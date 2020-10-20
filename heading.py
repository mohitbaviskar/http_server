import datetime
from resource import *
import os.path
from socket import *
root = "./cakesite"

#================================================================
# file_pointer => will be pointing to required file if it exists
# status_code_det => will have the status code for given request
#===================================================================


# request = input()
# req_list = request.split()

def head_response(req_list):
    print(req_list)

    #if just have to check the root dir.

    if req_list[1] == '/':
        html_file_check = root + "/index.html"
        #php_file_check = root + "/index.php"
        if os.path.exists(html_file_check):
            file_name = html_file_check
            status_code_det = "200"
        # elif os.path.exists(php_file_check):
        #     file_name = php_file_check
        #     status_code_det = "200"
        else :
            status_code_det = "404"



    elif len(req_list[1]) > 1:

        path_to_check = root + req_list[1]
        if os.path.isdir(path_to_check):
            #checking if it directory 


            # if path_to_check[-1] == '/':
            #     html_file_check = path_to_check + "index.html"
            #     php_file_check = path_to_check + "index.php"
            # else:

            html_file_check = path_to_check + "/index.html"
            #php_file_check = path_to_check + "/index.php"
            if os.path.exists(html_file_check):
                file_name = html_file_check
                status_code_det = "200"
            # elif os.path.exists(php_file_check):
            #     file_name = php_file_check
            #     status_code_det = "200"
            else :
                status_code_det = "404"
        

        #checking if it is a file

        elif os.path.isfile(path_to_check):
            file_name = path_to_check
            status_code_det = "200"

        else:
            status_code_det = "400"



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

    elif(read_type == 'image'):
        body = b""
        with open(file_name, "rb") as file_pointer:
            byte = file_pointer.read(1)
            while byte != b"":
                # Do stuff with byte.
                body += byte
                byte = file_pointer.read(1)
    
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


    
    return response
#head_response(req_list)