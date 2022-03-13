#!/usr/bin/python3
import sys


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
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")



# ### -------------------------------------------------------------------
# MyCodeTitle  = "microPython ESP8266 ( 範例 )"
# MyCodeString = '''
# ###  microPython ESP8266 範例程式 ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")




# ### -------------------------------------------------------------------
# MyCodeTitle  = "microPython ESP8266 ( 範例 )"
# MyCodeString = '''
# ###  microPython ESP8266 範例程式 ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")




# ### -------------------------------------------------------------------
# MyCodeTitle  = "microPython ESP8266 ( 範例 )"
# MyCodeString = '''
# ###  microPython ESP8266 範例程式 ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")




