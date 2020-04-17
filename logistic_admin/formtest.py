print "Content-type: text/html\n\n";

import pymysql
import datetime
import json
import cgi

form = cgi.FieldStorage()

# from ordermake.html 
productName = request.form["name_goods"]

print(productName)
