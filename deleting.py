from resource import *
import os
from socket import *
from documentroot.permissions.file_permissions import *


root = "./documentroot"
root_for_file_delete = "documentroot"

# request = input()
# req_list = request.split()


def delete_response(req_list):
    path_to_check = root+req_list[1]

    if(os.path.isfile(path_to_check)):
        if(req_list[1] not in file_per):
            file_to_del = root_for_file_delete + req_list[1]
            os.remove(file_to_del)
            #del file_per[req_list[1]]
            status_code_det = "200"
        else:
            status_code_det = "405"
    elif(os.path.isdir(path_to_check)):
        if(req_list[1] not in dir_per):
            dir_to_rmv = root_for_file_delete + req_list[1]
            os.rmdir(dir_to_rmv)
            #del dir_per[req_list[1]]
            status_code_det = "200"
        else:
            status_code_det = "405"
    else:
        status_code_det = "204"

    
    response = "HTTP/1.1 "+ status_code_det + " " + status_dict[status_code_det] + "\r\n"
    response += get_date()
    response += "Server: Mohit's server/0.0.1 (Ubuntu)\r\n"
    response += "Content-Type: " + "None\r\n"
    response += "Content-Length: " + "0\r\n"
    response += "Connection: keep-alive\r\n\r\n"

    response = response.encode()

    # print(response)
    return response


# delete_response(req_list)
        

