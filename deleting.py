from resource import *
import os
from socket import *
from permissions.file_permissions import *
import datetime


from configparser import ConfigParser

parser = ConfigParser()
parser.read('server.conf')



root = parser.get('documentroot','documentroot')
ipadd = parser.get('HOST', 'host')

root_for_file_delete = "documentroot"

# request = input()
# req_list = request.split()


def delete_response(request):
    req_list = request.split()
    r = request.split('\r\n')
    length = 0
    path_to_check = root+req_list[1]

    if(os.path.isfile(path_to_check)):
        if(req_list[1] not in file_per):
            file_to_del = root_for_file_delete + req_list[1]
            os.remove(file_to_del)
            #del file_per[req_list[1]]
            status_code_det = "204"
        else:
            status_code_det = "405"
    elif(os.path.isdir(path_to_check)):
        if(req_list[1] not in dir_per):
            dir_to_rmv = root_for_file_delete + req_list[1]
            os.rmdir(dir_to_rmv)
            #del dir_per[req_list[1]]
            status_code_det = "204"
        else:
            status_code_det = "405"
    else:
        status_code_det = "501"

    
    response = "HTTP/1.1 "+ status_code_det + " " + status_dict[status_code_det] + "\r\n"
    response += get_date()
    response += "Server: Mohit's server/0.0.1 (Ubuntu)\r\n"
    response += "Content-Type: " + "None\r\n"
    response += "Content-Length: " + "0\r\n"
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

    # print(response)
    return response


# delete_response(req_list)
        

