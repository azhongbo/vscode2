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


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode microPython ESP8266 ( 範例 )"
MyCodeString = '''
###  microPython ESP8266 範例程式 ####

# Linux 下載燒錄工具
# 方式1 https://github.com/espressif/esptool
# 方式2 pip3 install esptool

# 下載 Firmware for ESP8266 boards 
# http://micropython.org/

# 清除 erase flsh
esptool.py --port /dev/ttyUSB0 erase_flash

# 燒錄 
esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash -fm dio -fs 32m 0x00000 esp8266-20190125-v1.10.bin
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)



# ### -------------------------------------------------------------------
# MyCodeTitle  = "microPython ESP8266 ( 範例 )"
# MyCodeString = '''
# ###  microPython ESP8266 範例程式 ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)




# ### -------------------------------------------------------------------
# MyCodeTitle  = "microPython ESP8266 ( 範例 )"
# MyCodeString = '''
# ###  microPython ESP8266 範例程式 ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)




# ### -------------------------------------------------------------------
# MyCodeTitle  = "microPython ESP8266 ( 範例 )"
# MyCodeString = '''
# ###  microPython ESP8266 範例程式 ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)




##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
