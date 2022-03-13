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
# MyCodeTitle  = "RyanCode Python matplotlib ( 範例 )"
# MyCodeString = '''
# ###  Python matplotlib 範例程式 ####
# ### file: mainCode_Python_matplotlib
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python matplotlib ( 範例 )"
# MyCodeString = '''
# ###  Python matplotlib 範例程式 ####
# ### file: mainCode_Python_matplotlib
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python matplotlib ( 範例 )"
# MyCodeString = '''
# ###  Python matplotlib 範例程式 ####
# ### file: mainCode_Python_matplotlib
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python matplotlib ( 範例 )"
# MyCodeString = '''
# ###  Python matplotlib 範例程式 ####
# ### file: mainCode_Python_matplotlib
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python matplotlib ( 範例 )"
# MyCodeString = '''
# ###  Python matplotlib 範例程式 ####
# ### file: mainCode_Python_matplotlib
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


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
runAllData(MyCodeTitle,MyCodeString,MyCodeName)









##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
