
#for guessing mimetype for content type
import mimetypes
import datetime
import hashlib
import time
import os.path

def get_mime_type(file):
  return mimetypes.guess_type(file)[0]


# def etag(file):
#   hash = hashlib.sha1()
#   last_modified = os.path.getmtime("servermain.py")
#   hash.update((str(last_modified)).encode())
#   return  "ETag: "+ "\"" + hash.hexdigest() +"\""

def get_date():
  cur_time = datetime.datetime.now()
  return ("Date: " + cur_time.strftime("%A") + ", "+ cur_time.strftime("%d") + " " +  cur_time.strftime("%b") + " " + cur_time.strftime("%Y") + " " + cur_time.strftime("%X") + " GMT\r\n")

status_dict = {"100": "Continue",
  "101": "Switching Protocols",
  "200": "OK",
  "201": "Created",
  "202": "Accepted",
  "203": "Non-Authoritative Information",
  "204": "No Content",
  "205": "Reset Content",
  "206": "Partial Content",
  "300": "Multiple Choices",
  "301": "Moved Permanently",
  "302": "Found",
  "303": "See Other",
  "304": "Not Modified",
  "305": "Use Proxy",
  "307": "Temporary Redirect",
  "400": "Bad Request",
  "401": "Unauthorized",
  "402": "Payment Required",
  "403": "Forbidden",
  "404": "Not Found",
  "405": "Method Not Allowed",
  "406": "Not Acceptable",
  "407": "Proxy Authentication Required",
  "408": "Request Timeout",
  "409": "Conflict",
  "410": "Gone",
  "411": "Length Required",
  "412": "Precondition Failed",
  "413": "Request Entity Too Large",
  "414": "Request-URI Too Long",
  "415": "Unsupported Media Type",
  "416": "Requested Range Not Satisfiable",
  "417": "Expectation Failed",
  "500": "Internal Server Error",
  "501": "Not Implemented",
  "502": "Bad Gateway",
  "503": "Service Unavailable",
  "504": "Gateway Timeout",
  "505": "HTTP Version Not Supported"}

# print(status_dict["405"])


# file404 = open('/documentroot/dir400/400.html')
# txt = file404.read()

# res_404 = "HTTP/1.1 404 Not Found\r\n" + get_date() + "Server: Mohit's server/0.0.1 (Ubuntu)\r\n" + "Connection: close\r\n\r\n"
