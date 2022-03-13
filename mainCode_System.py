#!/usr/bin/python3
import sys



# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode System ( 範例 )"
# MyCodeString = '''
# ###  System 範例程式 ####
# ### file: mainCode_System
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode System ( 範例 )"
# MyCodeString = '''
# ###  System 範例程式 ####
# ### file: mainCode_System
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode System ( 範例 )"
# MyCodeString = '''
# ###  System 範例程式 ####
# ### file: mainCode_System
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode System ( 範例 )"
# MyCodeString = '''
# ###  System 範例程式 ####
# ### file: mainCode_System
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( HTTPS SSL 憑證 )"
MyCodeString = '''
###  System HTTPS SSL 憑證 ####
### file: mainCode_System
## 產生憑證 ##
openssl req -x509 -new -nodes -sha256 -utf8 -days 3650 -newkey rsa:2048 -keyout cert.key -out cert.crt -config ssl.conf

## 基本設定檔 ssl.conf##
[req]
prompt = no
default_md = sha256
default_bits = 2048
distinguished_name = dn
x509_extensions = v3_req

[dn]
C = TW
ST = Taiwan
L = Taipei
O = MyCompanyName
OU = MIS Department
emailAddress = admin@mycompany.com
CN = test.mycompany.com

[v3_req]
subjectAltName = @alt_names

[alt_names]
DNS.1 = test.mycompany.com
IP.1 = 192.168.1.10

'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")





### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( jitsi Meeting 安裝 @Ubuntu )"
MyCodeString = '''
###  System jitsi Meeting 安裝 @Ubuntu ####
### file: mainCode_System
# 參考網址： https://www.vultr.com/docs/how-to-install-jitsi-meet-on-ubuntu-18-04-lts
# 設定電腦名稱
sudo hostnamectl set-hostname MyHostName
sudo sed -i 's/^127.0.1.1.*$/127.0.1.1 MyHostName.abc.com MyHostName/g' /etc/hosts
# 開啟防火牆
sudo ufw allow OpenSSH
sudo ufw allow http
sudo ufw allow https
sudo ufw allow in 10000:20000/udp
sudo ufw allow samba
sudo ufw enable
# 安裝相關套件
sudo apt update
sudo apt upgrade -y &amp;&amp; sudo shutdown -r now
sudo apt install -y gnupg
sudo apt install -y openjdk-8-jre-headless
echo "JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")" | sudo tee -a /etc/profile
source /etc/profile
sudo apt install -y nginx
sudo systemctl start nginx.service
sudo systemctl enable nginx.service
https_proxy=http://xx.xx.xx.xx:8000 wget -qO - https://download.jitsi.org/jitsi-key.gpg.key | sudo apt-key add -
sudo sh -c "echo 'deb https://download.jitsi.org stable/' > /etc/apt/sources.list.d/jitsi-stable.list"
sudo apt update -y
# 安裝 Jitsi Server (最新版本)
sudo apt-get install  jitsi-meet
# 安裝 Jitsi Server (2.0.51 版本)
sudo apt-get install jitsi-meet=2.0.5142-1 jitsi-videobridge2=2.1-376-g9f12bfe2-1  jicofo=1.0-644-1 jitsi-meet-web=1.0.4466-1 jitsi-meet-web-config=1.0.4466-1 jitsi-meet-prosody=1.0.4466-1 jitsi-meet-turnserver=1.0.4466-1
# 出現下列訊息，輸入網址 MyHostName.abc.com
# The value for the hostname that is set in Jitsi Videobridge installation.  │ 
# The hostname of the current installation:  
# 執行 cert 輸入管理者 Email
sudo /usr/share/jitsi-meet/scripts/install-letsencrypt-cert.sh
## keyin admin@abc.com
# 臨時加入憑證方式
# 檔案位置 /etc/jitsi/meet/xxx.crt
# Windows 使用管理者權限執行 certutil.exe -addstore root xxx.crt
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( Ubuntu ufw 設定 )"
MyCodeString = '''
###  System Ubuntu ufw 設定 ####
### file: mainCode_System

#!/bin/bash

## 參考資料  https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-18-04

echo y | ufw reset           ## 清空設定
ufw default deny incoming    ## 阻擋進入
ufw default allow outgoing   ## 允許出去

## 範例1
ufw allow http
ufw allow https
ufw allow in 10000:20000/udp

## 範例2
ufw allow from 192.168.1.5 to any port 22
ufw allow from 192.168.1.5 to any port 5432
ufw allow from 192.168.1.5 to any port 9000

## 範例3
# ufw allow OpenSSH
# ufw allow 6000:6007/tcp
# ufw allow from 192.168.1.5 to any port 22
# ufw allow from 192.168.1.0/24
# ufw allow from 192.168.1.0/24 to any port 22
# ufw allow in on eth1 to any port 3306
# ufw allow in on eth0 to any port 80

# ufw app list
# ufw show added
# ufw deny http
# ufw status numbered

ufw enable

#### ufw for docker (Ubuntu) ####

## 參考 https://blog.36web.rocks/2016/07/08/docker-behind-ufw.html

## ufw 加入 2375
ufw allow 2375/tcp
ufw reload

vi /etc/default/ufw
DEFAULT_FORWARD_POLICY="ACCEPT"   ##  DROP 改為 ACCEPT

vi /etc/default/docker
DOCKER_OPTS="--iptables=false"   # 在 DOCKER_OPTS 加上 --iptables=false

vi /etc/systemd/system/docker.service.d/behind-ufw.conf  ## 加入下面 service
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd --iptables=false -H fd://

vi /etc/ufw/before.rules
 ## 找到 *filter ，並在前面加入下列
*nat
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING ! -o docker0 -s 172.17.0.0/16 -j MASQUERADE
COMMIT

## 重新啟動 docker
service docker restart
systemctl daemon-reload
systemctl restart docker.service

## 重新開機
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")






### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( Ubuntu Jitsi Server )"
MyCodeString = '''
###  System 範例程式 ####
### file: mainCode_System

# 參考網址： https://www.vultr.com/docs/how-to-install-jitsi-meet-on-ubuntu-18-04-lts

# 設定電腦名稱
sudo hostnamectl set-hostname MyHostName
sudo sed -i 's/^127.0.1.1.*$/127.0.1.1 MyHostName.abc.com MyHostName/g' /etc/hosts

# 開啟防火牆
sudo ufw allow OpenSSH
sudo ufw allow http
sudo ufw allow https
sudo ufw allow in 10000:20000/udp
sudo ufw allow samba
sudo ufw enable

# 安裝相關套件
sudo apt update
sudo apt upgrade -y && sudo shutdown -r now

sudo apt install -y gnupg
sudo apt install -y openjdk-8-jre-headless

echo "JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")" | sudo tee -a /etc/profile
source /etc/profile

sudo apt install -y nginx
sudo systemctl start nginx.service
sudo systemctl enable nginx.service

https_proxy=http://xx.xx.xx.xx:8000 wget -qO - https://download.jitsi.org/jitsi-key.gpg.key | sudo apt-key add -
sudo sh -c "echo 'deb https://download.jitsi.org stable/' > /etc/apt/sources.list.d/jitsi-stable.list"
sudo apt update -y


# 安裝 Jitsi Server (最新版本)
sudo apt-get install  jitsi-meet

# 安裝 Jitsi Server (2.0.51 版本)
sudo apt-get install jitsi-meet=2.0.5142-1 jitsi-videobridge2=2.1-376-g9f12bfe2-1  jicofo=1.0-644-1 jitsi-meet-web=1.0.4466-1 jitsi-meet-web-config=1.0.4466-1 jitsi-meet-prosody=1.0.4466-1 jitsi-meet-turnserver=1.0.4466-1

# 出現下列訊息，輸入網址 MyHostName.abc.com
# The value for the hostname that is set in Jitsi Videobridge installation.  │ 
# The hostname of the current installation:  

# 執行 cert 輸入管理者 Email
sudo /usr/share/jitsi-meet/scripts/install-letsencrypt-cert.sh
## keyin admin@abc.com


# 臨時加入憑證方式
# 檔案位置 /etc/jitsi/meet/xxx.crt
# Windows 使用管理者權限執行 certutil.exe -addstore root xxx.crt

'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")






### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( Anaconda )"
MyCodeString = '''
###  System Anaconda ####
### file: mainCode_System

conda update conda #進行更新
conda env list     #已經安裝幾個虛擬環境
conda create --name myEnvName python=3.7  ##建立環境


source activate myEnvName
conda list   # list安裝套件
conda install numpy pandas tensorflow-gpu==1.15 jupyter
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")





### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( qemu androix-x86)"
MyCodeString = '''
###  System qemu androix-x86 ####
### file: mainCode_System
## https://www.youtube.com/watch?v=bz8FugjsHs8

## 安裝套件
sudo apt install -y build-essential libepoxy-dev libdrm-dev libgbm-dev libx11-dev libvirglrenderer-dev libpulse-dev libsdl2-dev libgtk-3-dev

## 下載 qemu
wget https://www.youtube.com/redirect?q=https%3A%2F%2Fdownload.qemu.org%2Fqemu-3.1.1.1.tar.bz2&redir_token=QUFFLUhqbFY4SVBjQlhHY29VVlM3M0lPVjMtVzR6dGFvd3xBQ3Jtc0trZVFnc18tNDRObk5BY2hDQXplVFNRcDR4T2FsTXJXcWZLeXB0Z21XbGV1dGJ2eGR3NGhKR0M3V3lGYVpnSFAxZTFBWDIyMW80Sm12ektPa0hURERKYkp3b1dITUV5ZDBNQjJBRmVzTm5wM0FoX0FOYw%3D%3D&event=video_description&v=bz8FugjsHs8


## 封裝 qumu
mkdir build
cd build/
../configure --with-sdlabi=2.0 --enable-sdl --enable-opengl --enable-virglrenderer --enable-system --enable-modules --audio-drv-list=pa --target-list=x86_64-softmmu --enable-kvm --enable-gtk
make

sudo apt install qemu-utils

## 建立 virtual hard disk:
qemu-img create -f qcow2 Android9.img 128G

## 設定群組
sudo adduser klcppp kvm
sudo !!sudo chmod 666 /dev/kvm

## 設定權限 vi /lib/udev/rules.d/99-kvm.rules
KERNEL=="kvm", GROUP="kvm", MODE="0666"

## 開始安裝
./x86_64-softmmu/qemu-system-x86_64 -boot d -cdrom "/sdb2/VirtualBoxVMs/android-x86_64-9.0-r2.iso" -enable-kvm -smp 2 -device virtio-vga,virgl=on  -net nic -net user,hostfwd=tcp::5555-:22 -cpu host -soundhw es1370 -m 2048 -display sdl,gl=on -hda Android9.img

## 開始運行 , 移除 CDROM
./x86_64-softmmu/qemu-system-x86_64 -boot c -enable-kvm -smp 2 -device virtio-vga,virgl=on  -net nic -net user,hostfwd=tcp::5555-:22 -cpu host -soundhw es1370 -m 4096 -display sdl,gl=on -hda Android9.img
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")





### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( Text OCR 文字辨識 安裝 Tesseract )"
MyCodeString = '''
###  System Text OCR 文字辨識 安裝 Tesseract  ####
### file: mainCode_System
# 安裝 Tesseract 4.x
sudo apt install tesseract-ocr

# 安裝 Developer Tools
sudo apt install libtesseract-dev

# 安裝其他需要前置的套件
sudo apt-get -y install g++
sudo apt-get -y install autoconf automake libtool
sudo apt-get -y install pkg-config
sudo apt-get -y install libpng-dev
sudo apt-get -y install libjpeg8-dev
sudo apt-get -y install libtiff5-dev
sudo apt-get -y install zlib1g-dev

# 如果需要training tool, 則需要安裝
sudo apt-get -y install libicu-dev
sudo apt-get -y install libpango1.0-dev
sudo apt-get -y install libcairo2-dev

# 安裝Leptonica
sudo apt-get install libleptonica-dev

# 為了幫助可以在command line 上直接執行Tesseract
sudo snap install --channel=edge tesseract

# 如我們要識別英文以及繁體中文
sudo apt-get install tesseract-ocr-eng tesseract-ocr-chi-tra
sudo apt-get install tesseract-ocr-jpn tesseract-ocr-chi-sim

## Python 
pip install pytesseract
pip install pillow

## 顯示版本
tesseract --version

## 顯示辨識語言
tesseract --list-langs
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( ubuntu nvidia gpu cuda tf pytorch 安裝 )"
MyCodeString = '''
###  System  ubuntu nvidia gpu cuda tf pytorch 安裝 ####
### file: mainCode_System


##### 安裝顯示卡 ##################################################
sudo apt remove --purge nvidia*                      # 移除顯示卡驅動
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get update
ubuntu-drivers devices                               # 顯示可以安裝的驅動程式
sudo apt-get install nvidia-driver-435               # 安裝驅動
sudo reboot

## 檢查相關訊息
nvidia-smi
nvidia-settings


##### 安裝 GCC  #################################################
sudo apt-get install gcc-7
sudo apt-get install g++-7

sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 10
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 20

sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-7 10
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 20

sudo update-alternatives --config gcc
sudo update-alternatives --config g++

update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1
update-alternatives --install /usr/bin/python python /usr/bin/python3.8 2

update-alternatives --config python



##### CUDA 10.1 安裝 ##################################################
sudo ./cuda_10.1.105_418.39_linux.run

## 編輯 ~/.bashrc
export PATH="/usr/local/cuda-10.1/bin:$PATH"
export LD_LIBRARY_PATH=/usr/local/cuda-10.1/lib64:$LD_LIBRARY_PATH

## 重新載入 bashrc
source ~/.bashrc

## 安裝 cuDNN
## 解壓縮後, 將 lib64/*  複製到/usr/local/cuda-10.1/lib64/
sudo cp cudnn-10.1-linux-x64-v7.6.5.32/cuda/lib64/* /usr/local/cuda-10.1/lib64/



##### CUDA 11.1 安裝 ##################################################
sudo ./cuda_11.1.1_455.32.00_linux.run

## 編輯 ~/.bashrc
export PATH="/usr/local/cuda-11.1/bin:$PATH"
export LD_LIBRARY_PATH=/usr/local/cuda-11.1/lib64:$LD_LIBRARY_PATH

## 重新載入 bashrc
source ~/.bashrc

## 安裝 cuDNN
## 解壓縮 cudnn-11.1-linux-x64-v8.0.5.39.tgz , 將 lib64/*  複製到/usr/local/cuda-10.1/lib64/
sudo cp cudnn-11.1/lib64/* /usr/local/cuda-11.1/lib64/



## 測試 , 顯示如下
nvcc -V
# nvcc: NVIDIA (R) Cuda compiler driver
# Copyright (c) 2005-2019 NVIDIA Corporation
# Built on Fri_Feb__8_19:08:17_PST_2019
# Cuda compilation tools, release 10.1, V10.1.105

##### 安裝 Pytorch 和 Tensorflow-GPU ###############################
conda install pytorch torchvision cudatoolkit=10.1 -c pytorch
conda install tensorflow-gpu==2.2.0
conda install nb_conda


##### 安裝 Anaconda3 ###############################################
## 安裝 for 個人 , 全部使用預設
./Anaconda3-2020.02-Linux-x86_64.sh

## 安裝 for 全部 , 路徑指定到 /opt/anaconda3
sudo ./Anaconda3-2020.02-Linux-x86_64.sh   ## 安裝 for 全部 , 路徑指到

##在 .bashrc 找到 Anaconda 的環境變數, 並且複製到 /root/.bashrc    ">>> conda initialize >>>"


##### 簡易測試 GPU ##################################################
import torch
torch.cuda.is_available()
torch.tensor(1.0).device  ## check is cpu
torch.tensor(1.0).cuda().device ## check is gpu

import tensorflow as tf
tf.test.is_gpu_available()


##### Python 其他安裝 ##################################################
conda install -c anaconda beautifulsoup4
pip install gTTS
pip install googletrans
pip install opencv-python
pip install pygame==2.0.0.dev6
pip install beautifulsoup4 sklearn pyautogui lxml requests lxml


##### Ubuntu 一般安裝 ##################################################
apt-get -y install xsel
apt-get -y install clonezilla smplayer git encfs net-tools nmon ibus-chewing ibus-table-cangjie3
apt-get -y install ubuntu-restricted-extras winff grsync clonezilla kazam mdadm shutter gnome-raw-thumbnailer ufraw-batch encfs k4dirstat nmon language-pack-zh-hant expect gimp git ibus ibus-chewing  libreoffice-l10n-zh-tw libreoffice-pdfimport p7zip p7zip-full p7zip-rar libjpeg62 smplayer mate-terminal dconf-editor 
apt-get -y install qml-module-qtquick-layouts qml-module-qtquick2 qml-module-qtquick-controls qml-module-qtquick-dialogs qml-module-qtquick-window2
apt-get -y install gameconqueror

##### Ubuntu VirtualBox 安裝 ##########################################
apt-get -y install virtualbox virtualbox-guest-utils virtualbox-guest-additions-iso virtualbox-qt squashfs-tools qemu

##### Ubuntu 網路工具安裝 ##############################################
apt-get -y install firefox uget curl remmina remmina-plugin-rdp remmina-plugin-vnc etherape lynx nbtscan net-tools nmap putty

##### Ubuntu Server 安裝 ##############################################
apt-get -y install tasksel openssh-server samba system-config-samba apache2 php7.2 php7.2-sqlite3  apache2-dev php7.2-ldap php7.2-curl sqlite3 



##### Ubuntu 啟動 ##############################################
######## 建立 /etc/xdg/autostart/chewing.desktop ######### 
[Desktop Entry]
Type=Application
Name=Autostart Script
Exec=chewing
Icon=system-run
X-GNOME-Autostart-enabled=true
Name[en_US]=chewing.desktop

######## 建立 /bin/chewing ###############################
sudo locale-gen zh_TW.UTF-8

sudo mount /dev/sda1 /sda1
sudo mount /dev/sda2 /sda2

gsettings set org.gnome.desktop.input-sources sources "[('xkb', 'us'), ('ibus', 'chewing'), ('ibus', 'table:cangjie3')]"
gsettings set org.gnome.shell favorite-apps "['firefox.desktop', 'org.gnome.Nautilus.desktop']"
gsettings set org.gnome.nautilus.preferences executable-text-activation "ask"

xrandr --output DVI-D-0 --primary
xrandr --output HDMI-1  --off
xrandr --output DVI-D-0 --mode 1280x960
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( Python Text 2 Speech 自動念文章 )"
MyCodeString = '''
###  System Python Text 2 Speech 自動念文章 ####
### file: mainCode_System
# !pip3 install gTTS pygame googletrans
# !sudo apt-get -y install xsel

import os , datetime
from sys import platform as _platform
from gtts import gTTS
import pygame , googletrans

translator = googletrans.Translator()

def speech_other():
    
    with os.popen("xsel -b") as myCommand:
        
        now = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        mp3 = now + ".mp3"
        
        x = ""
        for i in myCommand.readlines(): x+=i
        
        x=x.replace( chr(10) ," " ).replace( chr(10) ," " )
        
        x2 = translator.translate(x, dest='zh-tw').text
        

        fp = open("filename.html", "a")        
        fp.write(f"<h4>{now}</h4> {chr(10)}")         
        fp.write(f"<p>{x}</p>  {chr(10)}")
        fp.write(f"<p>{x2}</p> {chr(10)}")
        fp.write(f"<audio controls=controls style='width:60%'> <source src={mp3} type=audio/mpeg > </audio> <br><br> {chr(10)}")
        fp.write(f"<hr> <script>window.scrollTo(0, 200000000);</script> {chr(10)}")
        fp.close()
        
        tts=gTTS( text=x2 , lang='zh-TW' )
        tts.save("tmp.mp3")
        
        os.system(f"ffmpeg -i tmp.mp3 -filter:a atempo=1.7 {mp3}")
    
        #pygame.mixer.init()
        #pygame.mixer.music.load(mp3)
        #pygame.mixer.music.play()        

    
def speech_cht():
    with os.popen("xsel -b") as myCommand:
        
        now = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        mp3 = now + ".mp3"        
        
        x = ""
        for i in myCommand.readlines(): x+=i
        
        x=x.replace( chr(10) ," " ).replace( chr(10) ," " )
        x=x.replace("*","乘以").replace("x","乘以")
        x=x.replace("，",",").replace("。","").replace(')','').replace('(','').replace(' ','')
        x=x.replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ")

        fp = open("filename.html", "a")
        fp.write(f"<h4>{now}</h4> {chr(10)}")         
        fp.write(f"<p>{x}</p>  {chr(10)}")
        fp.write(f"<p>{x2}</p> {chr(10)}")
        fp.write(f"<audio controls=controls style='width:60%'> <source src={mp3} type=audio/mpeg > </audio> <br><br> {chr(10)}")
        fp.write(f"<hr> <script>window.scrollTo(0, 200000000);</script> {chr(10)}")
        fp.close()
        
        tts=gTTS( text=x , lang='zh-TW' )
        tts.save("tmp.mp3")
        
        os.system(f"ffmpeg -i tmp.mp3 -filter:a atempo=1.7 {mp3}")
        
        #pygame.mixer.init()
        #pygame.mixer.music.load(mp3)
        #pygame.mixer.music.play()        

if _platform == "linux" or _platform == "linux2":
    os.system("rm -f tmp.mp3")
    #speech_cht()  ## 中文播放器
    speech_other() ## 其他語言播放器
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( ffmpeg mp4 影片裁切.py )"
MyCodeString = '''
###  System mp4 影片裁切.py ####
### file: mainCode_System
import time,datetime
import os
##### 時間轉秒數 ############################################
def time_to_sec(t1):
    h,m,s = t1.strip().split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)
##### 執行命令 ############################################
def run_command(ffmpeg_command):
    with os.popen(ffmpeg_command) as myCommand:
        dataArray = myCommand.readlines()
        for data in dataArray:
            print(data)
### 第2版切影片程式 ############################################
def getCommend(path,video,t1,t2,common):
    t1 = t1.strip()
    t2 = t2.strip()
    
    ee = time_to_sec(t2) - time_to_sec(t1)

    h = ('000'+str( ee//3600)    )[-2:]
    m = ('000'+str( ee%3600//60 ))[-2:]
    s = ('000'+str( ee%3600%60  ))[-2:]
    
    ext  = video[-4:]
    name = video[:-4]    
    flag = t1.replace(':',".")+'-'+t2.replace(':',".")
    video2 = f"{name}-{flag}-{common}{ext}"


    with open('list.txt', 'w') as f:
        f.write("file 'temp.mp4'")
    
    #cmd1 = f"ffmpeg -ss {t1} -t {h}:{m}:{s} -i {video} -c copy {video2}"
    cmd1 = f"ffmpeg -y -ss {t1} -t {h}:{m}:{s} -i {path}{video} -c copy temp.mp4"
    cmd2 = f"ffmpeg -y -f concat -i list.txt -c copy {video2}"
    
    print("轉檔: "+cmd1)
    run_command(cmd1)
    
    print("重包: "+cmd2)
    run_command(cmd2)
    
    run_command("rm -f temp.mp4")
    run_command("rm -f list.txt")
### END 第1版切影片程式 ############################################

### 第2版切影片程式 ############################################
def getCommend2(value1,value2):
    path   = value2[0]
    video  = value2[1]
    common = value2[2]
    
    for i in range( len(value1) ):
        t1 = value1[i][0].strip()
        t2 = value1[i][1].strip()

        ee = time_to_sec(t2) - time_to_sec(t1)

        h = ('000'+str( ee//3600)    )[-2:]
        m = ('000'+str( ee%3600//60 ))[-2:]
        s = ('000'+str( ee%3600%60  ))[-2:]
        
        videoTmp1 = f"____myTempVideo1{i}.mp4"
        videoTmp2 = f"____myTempVideo2{i}.mp4"
        
        cmd1 = f"ffmpeg -y -ss {t1} -t {h}:{m}:{s} -i {path}{video} -c copy {videoTmp1}"
        print("轉檔: "+cmd1)
        run_command(cmd1)
        
        with open('____listT.txt', 'w') as f:
            f.write(f"file {videoTmp1}\\n")
        print("重包1: "+cmd1)
        cmd2 = f"ffmpeg -y -f concat -i ____listT.txt -c copy {videoTmp2}"
        run_command(cmd2)
        
        ## 產生外層重包 list
        with open('____list.txt', 'a') as f:
            f.write(f"file {videoTmp2}\\n")
        
    
    name   = video[:-4]   
    flag   = value1[0][0].replace(':',".") + '-' +  value1[-1][-1].replace(':',".")
    ext    = video[-4:]
    video2 = f"{name}-{flag}-{common}{ext}"
    
    cmd3 = f"ffmpeg -y -f concat -i ____list.txt -c copy {video2}"
    print("重包2: "+cmd3)
    run_command(cmd3)
    
    run_command("rm -f ____myTempVideo*.mp4")
    run_command("rm -f ____list.txt")
    run_command("rm -f ____listT.txt")
    
### END 第2版切影片程式 ############################################

## 操作, 裁切 00:10:00～00:20:10 並重新命名 ##
### v1版 ###
# path  = '../video/'
# video = 'TensorFlow-Day3.mp4'
# getCommend( path , video, "00:22:18" , "01:01:15" , 'CNN-Introduction' ) 


### v2版  一段時間擷取 ###
# getCommend2([ ["02:02:10" , "02:11:52"] ] , ['../video/','TensorFlow-Day3.mp4','CNN-Introduction']  )

### v2版  兩段時間擷取並合併 ###
# getCommend2([ ["02:02:10" , "02:11:52"],
#               ["02:34:43" , "02:44:28"]] , ['../video/','TensorFlow-Day3.mp4','CNN-Introduction']  )

### v2版  三段時間擷取並合併 ###
# getCommend2([ ["02:02:10" , "02:11:52"],
#               ["02:33:16" , "02:34:43"],
#               ["02:34:43" , "02:44:28"]] , ['../video/','TensorFlow-Day3.mp4','CNN-Introduction']  )

'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")






### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( windows firewall )"
MyCodeString = '''
###  System Win firewall ####
### file: mainCode_System
netsh advfirewall firewall delete rule name="MyNetwork"

:: allow VNC
netsh advfirewall firewall add rule name="MyNetwork"  dir=in  interface=any action=allow enable=yes profile=private protocol=TCP localport=5900 remoteip="192.168.0.1-192.168.0.254"

:: block in By IP
netsh advfirewall firewall add rule name="MyNetwork"  dir=in  interface=any action=block remoteip="1.0.0.0-192.168.0.1"
netsh advfirewall firewall add rule name="MyNetwork"  dir=in  interface=any action=block remoteip="192.168.0.255-254.254.254.254"

:: block out By IP
netsh advfirewall firewall add rule name="MyNetwork"  dir=in  interface=any action=block remoteip="1.0.0.0-192.168.0.1"
netsh advfirewall firewall add rule name="MyNetwork"  dir=in  interface=any action=block remoteip="192.168.0.255-254.254.254.254"

---WinXP---------------------------------------------------------------------------------------------------------------------
::netsh firewall delete portopening TCP 8080
::netsh firewall add portopening TCP 8080 HTTP8080 ENABLE custom 192.168.0.1

netsh firewall delete portopening TCP 139
netsh firewall delete portopening TCP 445

netsh firewall add portopening TCP 139 P139 ENABLE custom 192.168.0.1,192.168.0.13
netsh firewall add portopening TCP 445 P445 ENABLE custom 192.168.0.1,192.168.0.13
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( 建立 e2b )"
MyCodeString = '''
###  System 建立 e2b ####
### file: mainCode_System

# 進入目錄 _ISO/docs/linux_utils
執行 ./fmt.sh  or ./fmt_ntfs.sh

# defragfs
./defragfs /media/ubuntu/EASY2BOOT/_ISO/LINUX


'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( find copy 檔案 )"
MyCodeString = '''
###  System find copy 檔案 ####
### file: mainCode_System

## 搜尋和複製檔案
find /Projects/ -name '*.exe' | cpio -pdm /home/ubuntu/Downloads/

find ./ -name '*.ipynb' -exec cp "{}" /home/ubuntu/Documents/  \;
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( caja右鍵ssh )"
MyCodeString = '''
###  System caja右鍵ssh ####
### file: mainCode_System

ubuntu nautilus寫入sh路徑: ~/.local/share/nautilus/scripts
mate 寫入sh路徑: ~/.config/caja/scripts
sshpass -p Win3975999 ssh -X user@192.168.0.1 thunderbird
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")





### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( Ubuntu path 系統路徑 )"
MyCodeString = '''
###  System Ubuntu path 系統路徑 ####
### file: mainCode_System

# 自動執行路徑 / .destop 路徑 / 字形路徑
/etc/xdg/autostart
/usr/share/applications
/usr/share/fonts
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( Linux Raid )"
MyCodeString = '''
###  System Linux Raid ####
### file: mainCode_System

VBoxManage createhd --filename /ssd/a1.vdi --size 4096
VBoxManage createhd --filename /ssd/a2.vdi --size 4096

modprobe nbd
qemu-nbd -c /dev/nbd0 /ssd/a1.vdi
qemu-nbd -c /dev/nbd1 /ssd/a2.vdi

mdadm --create --verbose /dev/md0 --level=0 --raid-devices=2 /dev/nbd0 /dev/nbd1

mkfs.ext4 -F /dev/md0

mkdir -p /raiddisk1
mount /dev/md0 /raiddisk1
chown -R ubuntu-mate:ubuntu-mate /raiddisk1
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( sudo without passwd 免密碼 )"
MyCodeString = '''
###  System sudo without passwd 免密碼 ####
### file: mainCode_System

visudo
## 最後一行加入
user ALL=(ALL) NOPASSWD:ALL
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( ubuntu vino vnc setup )"
MyCodeString = '''
### file: mainCode_System
# set for windows vnc
gsettings list-recursively org.gnome.Vino

gsettings set org.gnome.Vino require-encryption false
gsettings set org.gnome.Vino vnc-password $(echo -n '1234'|base64)
gsettings set org.gnome.Vino prompt-enabled false
gsettings set org.gnome.Vino authentication-methods "['vnc']"


#set-up
vino-preferences

#run-on service
/usr/lib/vino/
./vino-server > /dev/null &
./vino-server --display=:0 > /dev/null &
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")





### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( firewall iptable2 )"
MyCodeString = '''
###  System firewall iptable2 ####
### file: mainCode_System
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
iptables -t nat -F
iptables -t mangle -F
iptables -F
iptables -X

#Allow Loopback Connections
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

## Drop Invalid Packets
iptables -A INPUT -m conntrack --ctstate INVALID -j DROP

## ACCEPT port 
iptables -A INPUT -i enx00e04c360317 -p tcp -s 192.168.0.10/32 --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -i enx00e04c360317 -p tcp -s 192.168.0.10/32 --dport 80 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT

## ACCEPT IP
iptables -A INPUT -i enx00e04c360317 -s 192.168.0.20/32 -j ACCEPT

## Block an IP Address
#iptables -A INPUT -s 192.168.2.0/24 -j DROP

## Block from interface
iptables -A INPUT -i enx00e04c360317 -j DROP
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( firewall iptable )"
MyCodeString = '''
###  firewall iptable 範例程式 ####
### file: mainCode_System

#### Firewall ############################################################
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
iptables -t nat -F
iptables -t mangle -F
iptables -F
iptables -X

#Allow Loopback Connections
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

#Allow Established and Related Incoming Connections
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

#Allow Established Outgoing Connections
iptables -A OUTPUT -m conntrack --ctstate ESTABLISHED -j ACCEPT

#Internal to External
#iptables -A FORWARD -i eth1 -o enp4s0 -j ACCEPT

#Drop Invalid Packets
iptables -A INPUT -m conntrack --ctstate INVALID -j DROP

#Allow All Incoming SSH
iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp --sport 22 -m conntrack --ctstate ESTABLISHED -j ACCEPT

#Allow Incoming SSH from Specific IP address or subnet
iptables -A INPUT -p tcp -s 192.168.10.0/24 --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp --sport 22 -m conntrack --ctstate ESTABLISHED -j ACCEPT

#Allow Outgoing SSH
iptables -A OUTPUT -p tcp --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -p tcp --sport 22 -m conntrack --ctstate ESTABLISHED -j ACCEPT

#Allow Incoming Rsync from Specific IP Address or Subnet
iptables -A INPUT -p tcp -s 192.168.10.0/24 --dport 873 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp --sport 873 -m conntrack --ctstate ESTABLISHED -j ACCEPT

#Allow All Incoming HTTPS
iptables -A INPUT -p tcp --dport 443 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp --sport 443 -m conntrack --ctstate ESTABLISHED -j ACCEPT

#Allow All Incoming HTTP and HTTPS
#iptables -A INPUT -p tcp -m multiport --dports 80,443 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
#iptables -A OUTPUT -p tcp -m multiport --dports 80,443 -m conntrack --ctstate ESTABLISHED -j ACCEPT

#Allow MySQL from Specific IP Address or Subnet
iptables -A INPUT -p tcp -s 192.168.10.0/24 --dport 3306 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp --sport 3306 -m conntrack --ctstate ESTABLISHED -j ACCEPT

#Allow MySQL to Specific Network Interface
iptables -A INPUT -i eth1 -p tcp --dport 3306 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -o eth1 -p tcp --sport 3306 -m conntrack --ctstate ESTABLISHED -j ACCEPT

#Allow All Incoming HTTP
iptables -A INPUT -p tcp --dport 80 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp --sport 80 -m conntrack --ctstate ESTABLISHED -j ACCEPT

#Block an IP Address
iptables -A INPUT -s 192.168.10.0/24 -j DROP
iptables -A INPUT -s 192.168.10.0/24 -j REJECT

#Block Connections to a Network Interface
iptables -A INPUT -i enp4s0 -s 192.168.10.0/24 -j DROP

##### MASQUERADE ###########################################################

## IP 偽裝轉送
iptables -t nat -A POSTROUTING -s 192.168.10.0/24 -o enp4s0 -d 192.168.1.10  -j MASQUERADE

## 封包轉送
iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to 192.168.1.10:80
iptables -t nat -A POSTROUTING -p tcp --dport 80 --dst 192.168.1.10 -j MASQUERADE

## save rule
iptables-save > /etc/network/iptables.rules
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( MySql install )"
MyCodeString = '''
###  Ubuntu 18.04 Mysql ####
### file: mainCode_System

https://kknews.cc/zh-tw/code/4oynkpg.html
Ubuntu 18.04 中我們可以安裝Mysql 8 ， Mysql 8 是兼容到Ubuntu 18.04的。
要在安裝Mysql 8 要先安裝一個「mysql-apt-config_0.8.10-1_all.deb」包，打開下載頁面以後，點擊頁面中的「Download」
下載完畢以後使用下面的命令安裝

sudo dpkg -i mysql-apt-config_0.8.10-1_all.deb

安裝過程中會讓你選擇Mysql 的版本，選中「Mysql Server & Cluster」,進入版本選擇頁
選中Mysql 8，再按Tab鍵選中「確定」，回車，回車後會回到上圖的介面，選中「OK」，再回車
然後執行下面的命令更新下系統
sudo apt update
sudo apt autoremove mysql-client mysql-server mysql-workbench --purge

老版本的Mysql卸載完成以後可以使用下面的命令安裝8.0版本。「mysql-workbench」是GUI的管理工具， 如果你的Ubuntu沒有桌面環境不要安裝這個包。
sudo apt install mysql-client mysql-server mysql-workbench

然後選擇密碼加密方式，選擇第二個，如果選擇第一個的話用Mysql Workbench連接的時候會不支持授權方式

安裝完成以後直接打開Mysql Workbench，點擊「Localhost Instance 3306」 就可以連接了，不再做任何配置。
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( PostgreSQL install )"
MyCodeString = '''
###  Ubuntu 18.04 安裝 PostgreSQL ####
### file: mainCode_System

## 安裝
sudo apt -y install postgresql postgresql-contrib phppgadmin pgadmin3

## 切換身份進入 postgres
su - postgres

#進入管理界面
psql

#管理界面裡面-設定密碼
\password postgres

#管理界面裡面-離開
\q


## 編輯 /etc/apache2/conf-available/phppgadmin.conf
## 修改 
#Require local
Require all granted


## 編輯 /etc/phppgadmin/config.inc.php
## 修改
#$conf['extra_login_security'] = true;
$conf['extra_login_security'] = false;

#重起服務
service postgresql restart

#網址
http://localhost/phppgadmin/

## Enable remote access to PostgreSQL server 
vi /etc/postgresql/10/main/postgresql.conf
listen_addresses = '*'

vi /etc/postgresql/10/main/pg_hba.conf
host    all             all             192.168.5.0/24          md5

'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( Timezone 時區 )"
MyCodeString = '''
###  System 設定 Timezone 時區  ####
### file: mainCode_System

timedatectl list-timezones 
timedatectl set-timezone Asia/Taipei
timedatectl
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( apt - proxy socks5 )"
MyCodeString = '''
######  System apt - proxy socks5 ######
### file: mainCode_System

## Linux Server
vi /etc/tsocks.conf
server = 10.12.25.5
server_port = 3128

## socks5 server
ssh -gD 3128 127.0.0.1

##   port maping
ssh -gL 8080:localhost:80 root@127.0.0.1
ssh -gR 6666:localhost:8080 root@127.0.0.1
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( squid proxy )"
MyCodeString = '''
###  System squid proxy ####
### file: mainCode_System

apt-get install squid squid-common 

subl /etc/squid

http_access allow localnet
http_access allow localhost

#http_access deny all
http_access allow all

acl localnet src 192.168.0.0/16



## nuget behind proxy ##
nuget.exe config -set http_proxy=http://my.proxy.address:port

## vscode extension behind proxy ##
code --proxy-server=http://myproxy.example.com:3128

## git  behind proxy ##
git config --global http.proxy http://my.proxy.address:8080

## apt  behind proxy ##
vi /etc/apt/apt.conf
Acquire::http::Proxy "http://my.proxy.address:8080";

## docker  behind proxy ##
mkdir -p /etc/systemd/system/docker.service.d
vi /etc/systemd/system/docker.service.d/proxy.conf
[Service]
Environment="HTTP_PROXY=http://my.proxy.address:8080"
Environment="HTTPS_PROXY=http://my.proxy.address:8080"

#重起服務
systemctl daemon-reload
systemctl restart docker

'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( ubuntu gsettings 設定 )"
MyCodeString = '''
###  System ubuntu gsettings 設定 ####
### file: mainCode_System
sudo locale-gen zh_TW.UTF-8

#搜尋
gsettings list-recursively | grep chew

#輸入法 / 左邊 icon / 點擊 sh 檔案確認 / idle 設定
gsettings set org.gnome.desktop.input-sources sources "[('xkb', 'us'), ('ibus', 'chewing')]"
gsettings set org.gnome.shell favorite-apps "['firefox.desktop', 'shutter.desktop', 'libreoffice-calc.desktop', 'mate-terminal.desktop', 'code.desktop', 'caja.desktop']"
gsettings set org.gnome.nautilus.preferences executable-text-activation "ask"
gsettings set org.gnome.desktop.screensaver idle-activation-enabled false
gsettings set org.gnome.desktop.session idle-delay 0
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode System ( num 流水號 )"
MyCodeString = '''
###  System num 流水號 ####
### file: mainCode_System
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")







