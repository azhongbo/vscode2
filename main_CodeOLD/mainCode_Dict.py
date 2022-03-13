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
# MyCodeTitle  = "RyanCode xx Dictionary 字典"
# MyCodeString = '''
# ### xx Dictionary 字典 ####
# ### 檔案: mainCode_Dict
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode xx Dictionary 字典"
# MyCodeString = '''
# ### xx Dictionary 字典 ####
# ### 檔案: mainCode_Dict
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python Dictionary 字典"
MyCodeString = '''
### Python Dictionary 字典 ####
### 檔案: mainCode_Dict

movie = { 'name'     : 'Saving Private Ryan'                     ,  #電影名稱
          'year'     : 1998                                      ,  #電影上映年份
          'director' : 'Steven Spielberg'                        ,  #導演
          'Writer'   : 'Robert Rodat'                            ,  #編劇
          'Stars'    :['Tom Hanks', 'Matt Damon', 'Tom Sizemore'],  #明星
          'Oscar'    :['Best Director','Best Cinematography','Best Sound','Best Film Editing','Best Effects, Sound Effects Editing']
        }

print( movie['director'] )

'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode C# Dictionary 字典"
MyCodeString = '''
### C# Dictionary 字典 ####
### 檔案: mainCode_Dict

// Dictionary<key值,  value值> 字典名稱 = ...
   Dictionary<string, string> names = new Dictionary<string, string>();
   names.Add("張三", "1年級");
   names.Add("李四", "2年級");
   names.Add("王五", "3年級");
   string name = "李四";
  MessageBox.Show(names[name]);
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)









##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
