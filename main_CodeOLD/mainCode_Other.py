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
MyCodeTitle  = "RyanCode Other ( Except telnet / Perl命令列 )"
MyCodeString = '''
###  Perl 命令列傳入 ####
my ($str);
foreach $str (@ARGV){ push @key , $str; }



###  Python Except 自動 telnet ####
#!/usr/bin/expect -f
set timeout 3
set ip [lindex $argv 0]
spawn telnet $ip
expect "Password: "
send "password\\r"
expect '>'
send "show arp\\r"
send "                                                                          \\r"
send "                                                                          \\r"
send "                                                                          \\r"
send "exit\\r"
expect eof
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)




# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Other ( 範例 )"
# MyCodeString = '''
# ###  DOS 範例程式 ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)




# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Other ( 範例 )"
# MyCodeString = '''
# ###  DOS 範例程式 ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)




# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Other ( 範例 )"
# MyCodeString = '''
# ###  DOS 範例程式 ####
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)





##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
