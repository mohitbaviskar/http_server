#================================================
#this is for knowing the name filesystem
#=============================================
# import os.path
# root = "./ristorante-con-fusion/index.html"


# if os.path.isfile(root):
#     f = open(root)
#     print(f.read())
# import os
#=========================================

#====================================================
#this one below is for getting last modified time 
#=======================================================
# import datetime

# last_modified = os.path.getmtime("httpserver.py")
#                 #response += ("Last-Modified: " + last_modified.strftime("%A") + ", " + last_modified.strftime("%d") +  " " + last_modified.strftime("%b") + " " + last_modified.strftime("%Y") + " " + last_modified.strftime("%X") +  " GMT\n")
# response = ("last-Modified: " + datetime.datetime.fromtimestamp(last_modified).strftime("%A, %d %b, %Y %I:%M:%S")+ " GMT\n")
# print(response)
#=================================================================

#====================================================================
#for guessing mimetype for content type
import mimetypes

print(mimetypes.guess_type("logo.gif")[0])
#=====================================================================

# i = 33
# print(type(str(33)))