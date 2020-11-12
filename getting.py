
from resource import *
import os.path
from socket import *
from headercheck import *
from permissions.file_permissions import *
import datetime

from configparser import ConfigParser

parser = ConfigParser()
parser.read('server.conf')



root = parser.get('documentroot','documentroot')
ipadd = parser.get('HOST', 'host')

proxyfilelist = parser.get('PROX','prox')
#================================================================
# file_pointer => will be pointing to required file if it exists
# status_code_det => will have the status code for given request
#===================================================================


# request = input()
# req_list = request.split()

def get_response(req):
    r = req.split('\r\n')
    req_list = req.split()
    #print(req_list)
    need_for_file = 1
    file_name = ""
    cook = 0
    body = ""
    encbody = b""
    length = 0
    hostclear = 0
    cook = 0
    status_code_det = "200"
    #if just have to check the root dir.
    host_res = hostcheck(req_list)
    if host_res == 1:
        need_for_file = 1
        hostclear = 1
    else:
        need_for_file = 0
        status_code_det = "400"
    

    cookieresult = cookiecheck(req_list)
    if cookieresult != 1:
        cook = 1

    if(need_for_file == 1):
        if req_list[1] == '/':
            html_file_check = root + "/index.html"
            if os.path.exists(html_file_check):
                if html_file_check in proxyfilelist:#checking if file is in proxy server
                        if proxy_authorize(req_list):#proxy authorization check
                            file_name = html_file_check
                            status_code_det = "200"
                        else:
                            status_code_det = "407"
                            need_for_file = 0
                elif html_file_check in authorized:#checking if file is in server
                        pass_auth = www_authorize(req_list) 
                        if pass_auth == 1:# authorization check
                            # auth = 1
                            # user = user_auth
                            file_name = html_file_check
                            status_code_det = "200"
                        else:
                            status_code_det = "401"
                            need_for_file = 0
                else:
                    file_name = html_file_check
                    status_code_det = "200"
            elif html_file_check in temporary:
                    status_code_det = "307"
                    need_for_file = 0
                    location_of_file = temporary[html_file_check]
            elif html_file_check in permanent:
                    status_code_det = "301"
                    need_for_file = 0
                    location_of_file = permanent[html_file_check]
            else :
                status_code_det = "404"
                need_for_file = 0



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
                    if html_file_check in proxyfilelist:#checking if file is in proxy server
                        if proxy_authorize(req_list):#proxy authorization check
                            file_name = html_file_check
                            status_code_det = "200"
                        else:
                            status_code_det = "407"
                            need_for_file = 0
                    elif html_file_check in authorized:#checking if file is in server
                        pass_auth = www_authorize(req_list) 
                        if pass_auth == 1:# authorization check
                            # auth = 1
                            # user = user_auth
                            file_name = html_file_check
                            status_code_det = "200"
                        else:
                            status_code_det = "401"
                            need_for_file = 0                    
                    else:
                        file_name = html_file_check
                        status_code_det = "200"
                elif html_file_check in temporary:
                    status_code_det = "307"
                    need_for_file = 0
                    location_of_file = temporary[html_file_check]
                elif html_file_check in permanent:
                    status_code_det = "301"
                    need_for_file = 0
                    location_of_file = permanent[html_file_check]
                else :
                    status_code_det = "404"
                    need_for_file = 0
            

            #checking if it is a file

            elif os.path.isfile(path_to_check):
                if path_to_check in proxyfilelist:#checking if file is in proxy server
                        if proxy_authorize(req_list):#proxy authorization check
                            file_name = path_to_check
                            status_code_det = "200"
                        else:
                            status_code_det = "407"
                            need_for_file = 0
                elif path_to_check in authorized:#checking if file is in server
                        pass_auth = www_authorize(req_list) 
                        if pass_auth == 1:# authorization check
                            #auth = 1
                            # user = user_auth
                            file_name = path_to_check
                            status_code_det = "200"
                        else:
                            status_code_det = "401"
                            need_for_file = 0
                else:
                    file_name = path_to_check
                    status_code_det = "200"
            elif path_to_check in temporary:#check for temporarily moved
                    status_code_det = "307"
                    need_for_file = 0
                    location_of_file = temporary[path_to_check]
            elif path_to_check in permanent:
                    status_code_det = "301"
                    need_for_file = 0
                    location_of_file = permanent[path_to_check]
            else:
                status_code_det = "404"
                need_for_file =0
        
    if(need_for_file == 1):
        if_modi_ans = if_modi_since(req_list,file_name)
        if(if_modi_ans == 1):
            need_for_file = 0
            status_code_det = "304"


    response = "HTTP/1.1 "+ status_code_det + " " + status_dict[status_code_det] + "\r\n"
    response += get_date()
    response += "Server: Mohit's server/0.0.1 (Ubuntu)\r\n"
    #print(file_name)


    if(need_for_file == 1):
        # etagval = etag(file_name)
        encode_type = "gzip"
    
        mime_type = get_mime_type(file_name)
        read_type = mime_type.split('/')[0]

        if(read_type == 'text'):
            file_pointer = open(file_name)
            body = file_pointer.read()
            encbody = body.encode()
            length = len(encbody)
            # encode_type,body = encode_set(body,req_list)
        elif(read_type == 'image'):
            encbody = b""
            with open(file_name, "rb") as file_pointer:
                byte = file_pointer.read(1)
                while byte != b"":
                    # Do stuff with byte.
                    encbody += byte
                    byte = file_pointer.read(1)
            length = len(encbody)

        if(mime_type == 'None'):
            encbody = b""
            with open(file_name, "rb") as file_pointer:
                byte = file_pointer.read(1)
                while byte != b"":
                    # Do stuff with byte.
                    encbody += byte
                    byte = file_pointer.read(1)
                    length = len(encbody)

        response += "Content-Type: " + mime_type + "\r\n"
        response += "Content-Length: " + str(length) + "\r\n"
        # response += "Content-Encoding: " + encode_type + "\r\n"
        # response += etagval + "\r\n"

        # if(check_for_rangeheader(req_list) != 0):

        
    if(need_for_file == 1 or status_code_det == "304"):
        last_modified = os.path.getmtime(file_name)
        response += ("last-Modified: " + datetime.datetime.fromtimestamp(last_modified).strftime("%a, %d %b, %Y %I:%M:%S")+ " GMT\r\n")

    if(cook == 1):
        response += cookieresult

    if(status_code_det == "407"):#adding proxy autherntication header
        response += "Proxy-Authenticate: Basic\r\n"

    if(status_code_det == "401"):#adding proxy autherntication header
        response += "WWW-Authenticate: Basic\r\n"

    if(status_code_det == "307" or status_code_det == "301"):#adding location for temporaryily moved
        response += "Location: "+location_of_file+"\r\n"

    #access log 
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

    response += "Connection: close\r\n\r\n"
    print(response)
    response = response.encode()
    if(need_for_file == 1 and status_code_det != "304" ):
        response_enc = response + encbody
        return response_enc
    else:
        return response


    # print(response_enc)
    
#get_response(req_list)

