#!/usr/bin/python3
import sys

# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Other ( 範例 )"
# MyCodeString = '''
# ###  範例程式 ####
# ### file: mainCode_Other
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Other ( 範例 )"
# MyCodeString = '''
# ###  範例程式 ####
# ### file: mainCode_Other
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Other ( 範例 )"
# MyCodeString = '''
# ###  範例程式 ####
# ### file: mainCode_Other
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Other ( Except telnet / Perl命令列 )"
MyCodeString = '''
###  Perl 命令列傳入 ####
### file: mainCode_Other

my ($str);
foreach $str (@ARGV){ push @key , $str; }
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Other ( expect 自動 telnet )"
MyCodeString = '''
###  expect 自動 telnet ####
### file: mainCode_Other
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
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


