#!/usr/bin/python3
import sys
from __save__ import *

########################################################
def runAllData(MyCodeTitle,MyCodeString,MyCodeName):
    global package1,package2,extension,count

    count = count + 1    

    (data1,data2,data3) = makeCode(MyCodeTitle,MyCodeString,MyCodeName+str(count))

    package1  = package1  + data1
    package2  = package2  + data2
    extension = extension + data3
########################################################


package1   = ""
package2   = ""
extension  = ""
count      = 0
MyCodeName = sys.argv[2]




# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode NodeJS ( 範例 )"
# MyCodeString = '''
# ###  Python NodeJS ####
# ### file: mainCode_Nodejs
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)



# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode NodeJS ( 範例 )"
# MyCodeString = '''
# ###  Python NodeJS ####
# ### file: mainCode_Nodejs
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)



# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode NodeJS ( 範例 )"
# MyCodeString = '''
# ###  Python NodeJS ####
# ### file: mainCode_Nodejs
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)



# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode NodeJS ( 範例 )"
# MyCodeString = '''
# ###  Python NodeJS ####
# ### file: mainCode_Nodejs
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)






### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode NodeJS ( Electron 環境建制 )"
MyCodeString = '''
###  Python NodeJS Electron 環境建制 ####
### file: mainCode_Nodejs

安裝軟體:
Nodejs  / Git / Visual Studio Build Tools 2017

NPM 環境設定:
npm config set msvs_version 2017
npm config set python C:\Users\user\.windows-build-tools\python27\python.exe

npm install -g node-gyp
:: npm install --global --production windows-build-tools@4.0.0

npm install electron-prebuilt -g
npm install electron-prebuilt --save-dev

npm install electron-packager -g
npm install electron-packager --save-dev

npm i patch-package
npm i patch-package  --save-dev

npm install -g asar


npm install

npm i robotjs

npm run postinstall
npm run dist





'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)








##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
