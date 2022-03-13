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
# MyCodeTitle  = "RyanCode DateTime ( 範例 )"
# MyCodeString = '''
# ###  C# 範例 範例程式 ####
# ### 檔案: mainCode_DateTime
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)



# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode DateTime ( 範例 )"
# MyCodeString = '''
# ###  C# 範例 範例程式 ####
# ### 檔案: mainCode_DateTime
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)



# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode DateTime ( 範例 )"
# MyCodeString = '''
# ###  C# 範例 範例程式 ####
# ### 檔案: mainCode_DateTime
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)






### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode DateTime ( PHP 範例 )"
MyCodeString = '''
## php 時間日期
### 檔案: mainCode_DateTime

$date = date("Y-m-d H:i:s", time() - ( 0 * 24 * 60 * 60 ) );

## php 兩個日期相減
$nn = ( strtotime($date1) - strtotime($date2) ) / 3600 / 24;
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode DateTime ( Perl 範例 )"
MyCodeString = '''
## Perl 時間日期
### 檔案: mainCode_DateTime

$myTime = time() - 0 * 24 * 3600;
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($myTime);
$mon+=1;
$year=$year + 1900;
$min  = '0'.$min  if length($min)  < 2;
$sec  = '0'.$sec  if length($sec)  < 2;
$mon  = '0'.$mon  if length($mon)  < 2;
$mday = '0'.$mday if length($mday) < 2;
$hour = '0'.$hour if length($hour) < 2;
$year = '0'.$year if length($year) < 2;

## Perl 兩個日期相減
use POSIX qw(mktime);
use POSIX qw(difftime);
$kk = &diff_date("2014/11/12","2014/11/13");
sub diff_date()
    {
        my @t1 = split( "/" , $_[0] );
        $year = @t1[0] - 1900;
        $mon  = @t1[1] - 1;
        $mday = @t1[2];
        $sec  = 00;
        $min  = 00;
        $hour = 00;
        my $start = mktime ($sec,$min,$hour,$mday,$mon,$year);
        my @t2 = split( "/" , $_[1] );
        $year = @t2[0] - 1900;
        $mon  = @t2[1] - 1;
        $mday = @t2[2];
        $sec  = 00;
        $min  = 00;
        $hour = 00;
        my $end = mktime ($sec,$min,$hour,$mday,$mon,$year);
        my $result = difftime($end, $start);
        print $result/(24*60*60),"\n";
    }
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode DateTime ( Python 範例 )"
MyCodeString = '''
## Python 時間日期
### 檔案: mainCode_DateTime

myTime = time.strftime('%Y%m%d %H%M%S %w %j %U',time.localtime(time.time() + i * 24 * 60 * 60 ) )
year = myTime[0:4] ## %Y 四位數的年份表示（000-9999）
mon  = myTime[4:6] ## %m 月份（01-12）
mday = myTime[6:8] ## %d 月内中的一天（0-31）

hour = myTime[9:11] ## %H 24小時製小時數（0-23）
min  = myTime[11:13] ## %M 分鐘數（00=59）
sec  = myTime[13:15] ## %S 秒（00-59）

dweek = myTime[16:17] ## %w 星期（0-6），星期天為星期的開始
dyear = myTime[18:21] ## %j 年内的一天（001-366）
nweek = myTime[22:24] ## %U 一年中的星期數（00-53），星期天為星期的開始

## 兩個日期相差天數
d1 = datetime.datetime(2016, 01, 01)
d2 = datetime.datetime(2015, 01, 01)
#print (d1-d2).days

## 兩個時間秒差
starttime = datetime.datetime.now()
endtime = datetime.datetime.now()
#print (endtime - starttime).seconds

## 計算10天後的時間
d1 = datetime.datetime.now()
d3 = d1 + datetime.timedelta(days =10)

## %y 两位數的年份表示（00-99）
## %Y 四位數的年份表示（000-9999）
## %m 月份（01-12）
## %d 月内中的一天（0-31）
## %H 24小時製小時數（0-23）
## %I 12小時製小時數（01-12）
## %M 分鐘數（00=59）
## %S 秒（00-59）
## %a 本地簡化星期名稱
## %A 本地完整星期名稱
## %b 本地簡化的月份名稱
## %B 本地完整的月份名稱
## %c 本地相應的日期表示和時間表示
## %j 年内的一天（001-366）
## %p 本地A.M.或P.M.的等價符
## %U 一年中的星期數（00-53），星期天為星期的開始
## %w 星期（0-6），星期天為星期的開始
## %W 一年中的星期數（00-53）星期一為星期的開始
## %x 本地相應的日期表示
## %X 本地相應的時間表示
## %Z 當前時區的名稱
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)





### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode DateTime ( C# 範例 )"
MyCodeString = '''
###  C# 時間日期 ####
### 檔案: mainCode_DateTime

DateTime dt1 = DateTime.Now;
DateTime dt2 = DateTime.Now.AddMinutes(30);
            
string cc = DateTime.Now.ToString("yyyy-MM-dd hh:mm:ss");
string dd = DateTime.Now.AddMinutes(5).ToString("yyyy-MM-dd hh:mm:ss");
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)














##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
