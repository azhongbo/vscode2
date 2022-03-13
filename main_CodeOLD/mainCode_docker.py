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
MyCodeTitle  = "RyanCode Docker ( download command 命令 )"
MyCodeString = '''
###  Docker command 命令 ####
### 檔案: Dockerfile

docker pull tomcat:jre-9  ## 下載 tomcat
docker pull ubuntu  ## 下載 ubuntu
docker images ## 列出 images 
docker ps ## 列出執行中的 image

docker run -it --rm ubuntu bash

'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Docker ( Dockfile Ubuntu PHP 7.4 )"
MyCodeString = '''
###  Docker Ubuntu PHP 7.4 ####
### 檔案: Dockerfile

FROM ubuntu
COPY startHttp /bin
RUN chmod 755 /bin/startHttp

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata
RUN ln -sf /usr/share/zoneinfo/Asia/Taipei /etc/localtime
RUN apt-get -y install net-tools nmap apache2 php7.4 curl systemd php7.4-sqlite3 apache2-dev php7.4-ldap php7.4-curl sqlite3 php7.4-curl php7.4-gd php7.4-pgsql php7.4-xml php7.4-bz2 php7.4-mbstring iputils-ping vim

RUN echo "ServerName localhost:80" >> /etc/apache2/apache2.conf

RUN echo "Asia/Taipei" > /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata
RUN echo "Asia/Taipei" > /etc/timezone

RUN apt-get -y install python3 python3-pip python3-tk python3-dev scrot
RUN python3 -m pip install beautifulsoup4 flask jupyter jupyterlab keras lxml matplotlib numpy opencv-python pandas plotly pyautogui pygame pymssql python3-xlib requests selenium sklearn xlrd tensorflow==2.4.1
RUN python3 -m pip install torch==1.8.0+cpu torchvision==0.9.0+cpu torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html
# RUN python3 -m pip install psycopg2

EXPOSE 80
CMD ["startHttp"]





### 檔案: startHttp
#!/bin/bash
apachectl -D FOREGROUND


### 封裝 built 和 執行 run
docker built -t UbuntuPHP74 .
docker run -it --rm UbuntuPHP74 bash
docker run -dit --rm -p 80:80 -v /usr/local/docker/UbuntuPHP74/html:/var/www/html --name php UbuntuPHP74 startHttp
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Docker ( save load images 匯出匯入 )"
MyCodeString = '''
###  Docker save load images 匯出匯入 ####
### 檔案: Dockerfile

docker save -o <path for generated tar file> <image name>
docker load -i <path to image tar file>
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)




# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Docker ( 範例 )"
# MyCodeString = '''
# ###  Docker 範例程式 ####
### 檔案: Dockerfile
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)




# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Docker ( 範例 )"
# MyCodeString = '''
# ###  Docker 範例程式 ####
### 檔案: Dockerfile
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)





##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
