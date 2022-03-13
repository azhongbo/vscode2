#!/usr/bin/python3
import sys





# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python flask ( 範例 )"
# MyCodeString = '''
# ###  Python flask 範例程式 ####
# ### file: mainCode_Python_flask
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python flask ( 範例 )"
# MyCodeString = '''
# ###  Python flask 範例程式 ####
# ### file: mainCode_Python_flask
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python flask ( 範例 )"
# MyCodeString = '''
# ###  Python flask 範例程式 ####
# ### file: mainCode_Python_flask
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")




## -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python flask ( 網頁傳 json )"
MyCodeString = '''
###  Python  flask 網頁傳 json  ####
# ### file: mainCode_Python_flask

-*-  coding:utf-8  -*-
import pandas as pd
from flask import Flask , render_template
import json

jasonData = {"name":"Ryan","home":"Taipe"}  ## Step1: json 格式
myString  = json.dumps(jasonData)           ## Step2: json 轉字串 

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('test.html' , jsonData = myString )

if __name__ == "__main__":
    #app.debug = True
    app.run( host='0.0.0.0',port=5000)


###### HTML templates/test.html ########################################
<div id=myData>{{ jsonData }}</div>
<div id=data1></div>
<div id=data2></div>

<script src="https://code.jquery.com/jquery-1.12.4.js"
integrity="sha256-Qw82+bXyGq6MydymqBxNPYTaUXXq7c8v3CwiYwLLNXU="
crossorigin="anonymous"></script>

<script>
var data = $.parseJSON( $("#myData").html() )
$("#data1").html(data.name)
$("#data2").html(data.home)
</script>
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")




## -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python flask ( send file to downlad )"
MyCodeString = '''
###  Python flask downlad ####
# ### file: mainCode_Python_flask

-*-  coding:utf-8  -*-
import os
# from flask import Flask, request, abort, jsonify, send_from_directory
# from flask import send_file
from flask import *

app = Flask(__name__)

@app.route('/files/')
def return_files_tut():
	try:
		return send_file('/files/P1040406.MOV', attachment_filename='P1040406.MOV.aa')
	except Exception as e:
		return str(e)

@app.route("/files/<filepath>", methods=['GET'])
def download_file(filepath):
    # 此处的filepath是文件的路径，但是文件必须存储在static文件夹下， 比如images\test.jpg
    return app.send_static_file(filepath)  

# http://localhost/files/P1040406.MOV


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python flask ( POST GET )"
MyCodeString = '''
###  Python flask POST GET ####
### file: mainCode_Python_flask

-*-  coding:utf-8  -*-
import os,sqlite3,random,socket,time
from flask import Flask , render_template 
from flask import *

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
@app.route( "/command" , methods=["POST","GET"] )
def auth():
    # HTML Form get #
    # search = request.args.get("search")
    # page = request.args.get("page")

    # HTML Form post
    username  = str( request.form.get("username") )

    return value

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(("127.0.0.1",5000))

if __name__ == "__main__" and result != 0:
    app.run(host="0.0.0.0" , port=5000 , debug=True)

if result == 0:
    print("already running")

'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")








