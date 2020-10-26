#response += "Set-Cookie: sdfsdfsd=332423423\r\n"

import secrets
import string

def cookiecheck(req_list):
    if 'Cookie:' in req_list:
        ind = req_list.index('Cookie:')
        val = req_list[ind + 1]
        res = cookiefilecheck(val)
        if res == 0:
            return 1
        else :
            return 0
    else:
        cookies = generate_cookie()
        f = open("documentroot/server_data/cookie.txt","a")
        f.write(cookies)
        f.close()
        response = 'Set-Cookie: ' + cookies
        return response



def generate_cookie():
    key = ''.join((secrets.choice(string.ascii_letters) for i in range(10)))
    value = ''.join((secrets.choice(string.ascii_letters) for i in range(10)))
    val = key+'='+value
    result = cookiefilecheck(val)
    while(result == 0):
        key = ''.join((secrets.choice(string.ascii_letters) for i in range(10)))
        value = ''.join((secrets.choice(string.ascii_letters) for i in range(10)))
        val = key+'='+value
        result = cookiefilecheck(val)
    return val + ' \n'


def cookiefilecheck(val):
    f = open("documentroot/server_data/cookie.txt","r+")
    t = f.read()
    t = t.split(' \n')
    for i in t:
        if(i == val):
            return 0
    return 1


