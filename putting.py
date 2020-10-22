
from resource import *
import os.path
from socket import *
from documentroot.permissions.file_permissions import *

root = "./documentroot"
root_for_file_create = "documentroot"
#request = input()

def put_response(request):
    req_list = request.split()
    put_list = request.split('\r\n\r\n')

    path_to_check = root + req_list[1]

    if (os.path.isfile(path_to_check)):
        if(req_list[1] not in file_per):
            f = open(path_to_check,"w")
            f.write(put_list[1])
            status_code_det = "200"
        else:
            status_code_det = "405"
    else:
        req = req_list[1].split('/')
        req1 = ('/').join(req[0:len(req)-1])
        path_to_check = root + req1
        if(os.path.isdir(path_to_check)):
            if(req1 not in dir_per):
                new_file = root_for_file_create + req_list[1]
                f = open(new_file,"w")
                f.write(put_list[1])
                status_code_det = "200"
            else:
                status_code_det = "405"
        else:
            status_code_det = "405"

    response = "HTTP/1.1 "+ status_code_det + " " + status_dict[status_code_det] + "\r\n"
    response += get_date()
    response += "Server: Mohit's server/0.0.1 (Ubuntu)\r\n"
    response += "Content-Type: " + "None\r\n"
    response += "Content-Length: " + "0\r\n"
    response += "Connection: keep-alive\r\n\r\n"

    response = response.encode()
    return response
    #print(response)

#put_response(request)

    
        


