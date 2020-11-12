#response += "Set-Cookie: sdfsdfsd=332423423\r\n"

import secrets
import string
import gzip
import string
import os
import io
import base64
import datetime
from permissions.file_permissions import *

from configparser import ConfigParser

parser = ConfigParser()
parser.read('server.conf')
proxyuserlist = parser.get('PROX','proxy_user')

def cookiecheck(req_list):
    if 'Cookie:' in req_list:
        return 1
    cookies = generate_cookie()
    response = 'Set-Cookie: ' + cookies
    return response


def www_authorize(req_list):
    if 'Authorization:' in req_list:
        ind = req_list.index('Authorization:')
        val = req_list[ind+2]
        h = base64.b64decode(val)
        print(h)
        h = h.decode()
        # base64.b64encode(val)
        if h in auth_pass:
            return 1
        else:
            return 0

def generate_cookie():
    key = ''.join((secrets.choice(string.ascii_letters) for i in range(10)))
    value = ''.join((secrets.choice(string.ascii_letters) for i in range(10)))
    val = key+'='+value
    return val + ' \n'


def if_modi_since(req_list,filename):
    if 'If-Modified-Since:' in req_list:
        ind = req_list.index('If-Modified-Since:')
        ifmodval = req_list[ind+1] + " " + req_list[ind+2] + " " +req_list[ind+3] + " " + req_list[ind+4] + " " + req_list[ind + 5] + " " + req_list[ind+6]
        last_modified = os.path.getmtime(filename)
        fltime = (datetime.datetime.fromtimestamp(last_modified).strftime("%A, %d %b, %Y %I:%M:%S")+ " GMT")
        print(ifmodval)
        print(fltime)
        if(ifmodval == fltime):
            return 1
        else:
            return 0
    else:
        return 0

def hostcheck(req_list):
    if 'Host:' in req_list:
        return 1
    else:
        return 0



# def rangecheck(req_list):
#     if '' in req_list:
#         return 0
#     else:
#         return -1


# def encode_set(body,req_list):
#     # encode_list = [gzip,deflate,br]
#     if 'Accept-Encoding: ' in req_list:
#         return 0
#     else:
#         encode_type = "gzip"
#         # return encode_type,new_body
#         output = gzip.compress(body.encode())
#         return encode_type,output
        # new_body = gzip.compress(body.encode())
        

def proxy_authorize(req_list):
    print(req_list)
    if 'Proxy-Authorization:' in req_list:
        ind = req_list.index('Proxy-Authorization:')
        if req_list[ind + 1] in proxy_user:
            return 1
        else:
            return 0
    else:
        return 0