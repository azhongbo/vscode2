#!/usr/bin/python3
import sys





# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python matplotlib ( 範例 )"
# MyCodeString = '''
# ###  Python matplotlib 範例程式 ####
# ### file: mainCode_Python_matplotlib
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python matplotlib ( 範例 )"
# MyCodeString = '''
# ###  Python matplotlib 範例程式 ####
# ### file: mainCode_Python_matplotlib
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python matplotlib ( 範例 )"
# MyCodeString = '''
# ###  Python matplotlib 範例程式 ####
# ### file: mainCode_Python_matplotlib
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python matplotlib ( 範例 )"
# MyCodeString = '''
# ###  Python matplotlib 範例程式 ####
# ### file: mainCode_Python_matplotlib
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python matplotlib ( 範例 )"
# MyCodeString = '''
# ###  Python matplotlib 範例程式 ####
# ### file: mainCode_Python_matplotlib
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python matplotlib ( 中文亂碼處理 )"
MyCodeString = '''
###  Python matplotlib 中文亂碼處理 ####
### file: mainCode_Python_matplotlib
import numpy as np 
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

x = np.arange(1,11)
y =  2  * x +  5

plt.title("test")

font = FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc", size=14)

plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False

plt.xlabel("x axis caption 測試x",fontproperties=font )
plt.ylabel("y axis caption 測試y",fontproperties=font) 
plt.plot(x,y)
plt.show()
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")









