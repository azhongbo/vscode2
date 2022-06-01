#!/usr/bin/python3
import sys

# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Docker ( 範例 )"
# MyCodeString = '''
# ###  Docker 範例程式 ####
# ## 檔案: mainCode_docker
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Docker ( 範例 )"
# MyCodeString = '''
# ###  Docker 範例程式 ####
# ## 檔案: mainCode_docker
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Docker ( keep container running 保持運作 )"
MyCodeString = '''
###  Docker keep container running 保持運作 ####
## 檔案: mainCode_docker
sleep infinity

# vi docker-compose.yml
version: '3'
services:
  some-app:
    tty: true
    command: tail -f /dev/null

# vi Dockerfile
CMD sleep infinity
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Docker ( docker list all version 找到個版本 )"
MyCodeString = '''
###  Docker docker list all version 找到個版本 ####
## 檔案: mainCode_docker

## 搜尋 nginx/unit 版本
imageName=nginx/unit
wget -q https://registry.hub.docker.com/v1/repositories/$imageName/tags -O -  | sed -e 's/[][]//g' -e 's/"//g' -e 's/ //g' | tr '}' '\\n'  | awk -F: '{print $3}'
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Docker ( unit php )"
MyCodeString = '''
###  Docker unit php ####
## 檔案: mainCode_docker

## 官方網址  https://unit.nginx.org/installation/

### 使用 ubuntu 安裝方式 ############################################

apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata
ln -sf /usr/share/zoneinfo/Asia/Taipei /etc/localtime

echo "Asia/Taipei" > /etc/timezone
dpkg-reconfigure --frontend noninteractive tzdata
echo "Asia/Taipei" > /etc/timezone

apt-get install tzdata
dpkg-reconfigure tzdata

apt-get install vim systemd iftop net-tools nmon ufw curl wget

curl --output /usr/share/keyrings/nginx-keyring.gpg https://unit.nginx.org/keys/nginx-keyring.gpg

vi /etc/apt/sources.list.d/unit.list
deb [signed-by=/usr/share/keyrings/nginx-keyring.gpg] https://packages.nginx.org/unit/ubuntu/ focal unit
deb-src [signed-by=/usr/share/keyrings/nginx-keyring.gpg] https://packages.nginx.org/unit/ubuntu/ focal unit

wget http://launchpadlibrarian.net/398247488/perl-base_5.26.1-6ubuntu0.3_amd64.deb
sudo dpkg -i perl-base_5.26.1-6ubuntu0.3_amd64.deb

apt update
apt install unit
apt install unit-dev unit-go unit-jsc11 unit-perl unit-php unit-python2.7 unit-python3.8 unit-ruby
systemctl restart unit 

apt-get update
apt-get install unit
apt-get install -y -qq --no-install-recommends certbot ghostscript nginx \
php-bcmath php-cli php-common php-curl php-gd php-imagick php-mbstring php-mysql php-opcache \
php-xml php-zip python3-certbot-nginx unit unit-dev unit-go unit-jsc11 unit-perl unit-php \
unit-python2.7 unit-python3.8 unit-ruby
systemctl restart unit

docker commit containersId imageName

### 使用官方 docker images 方式 ###################################

## 搜尋 nginx/unit 版本
imageName=nginx/unit
wget -q https://registry.hub.docker.com/v1/repositories/$imageName/tags -O -  | sed -e 's/[][]//g' -e 's/"//g' -e 's/ //g' | tr '}' '\\n'  | awk -F: '{print $3}'

# 搜尋到以下版本，使用最後一個
## docker pull docker.io/nginx/unit:1.14.0-php7.3
## docker pull docker.io/nginx/unit:1.15.0-php7.3
## docker pull docker.io/nginx/unit:1.16.0-php7.3
## docker pull docker.io/nginx/unit:1.17.0-php7.3
## docker pull docker.io/nginx/unit:1.18.0-php7.3
## docker pull docker.io/nginx/unit:1.19.0-php7.3
## docker pull docker.io/nginx/unit:1.20.0-php7.3
docker pull docker.io/nginx/unit:1.21.0-php7.3

## 封裝 Containers
docker commit \
    --author "xxx@gmail.com" \
    --message "test" \
    e23743a1603f \
    myImageName:v1

docker commit e23743a1603f unit2:v2

## 啟動
docker run -it -p 80:80 \
-v /home/klcppp/ubuntu/app:/app \
-v /home/klcppp/ubuntu/app/unit:/etc/unit \
nginx/unit:1.21.0-php7.3 bash

## 編輯設定檔案
vi /etc/unit/start.json
{
    "listeners": 
    {
        "*:8081": 
        {
            "application": "infopage"
        },
        "*:8082": 
        {
            "application": "hellopage"
        }
    },
    "applications": 
    {
        "infopage": 
        {
            "type": "php",
            "processes": 2,
            "root": "/app/html",
            "index": "info.php"
        },
        "hellopage": 
        {
            "type": "php",
            "processes": 2,
            "root": "/app/html",
            "index": "hello.php"
        }
    }
}

curl -X PUT -d @start.json --unix-socket /var/run/control.unit.sock http://localhost/config/

## Web測試: wrk 測試效能 ## 
## wrk 是用C語言寫的http benchmark 工具，是一種簡易的HTTP 性能測試。

## 安裝
sudo apt-get install build-essential libssl-dev git -y
git clone https://github.com/wg/wrk.git wrk
cd wrk
sudo make
sudo cp wrk /usr/local/bin

## -t12 用 12 個線程 # -c400 模擬 400 個併發連接 # -d30s 持續 30 秒
wrk -t12 -c400 -d30s http://127.0.0.1:8081/

## Web測試: nikto 檢查網頁伺服器全問題的工具 ## 
git clone https://github.com/sullo/nikto

# Main script is in program/
cd nikto/program

# Run using the shebang interpreter
./nikto.pl -h http://www.example.com
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Docker ( nginx uwsgi flask )"
MyCodeString = '''
###  Docker nginx uwsgi flask ####
## 檔案: mainCode_docker

### docker-compose.yml ###############
services:
  flask:
    build: ./flask
    container_name: flask
    restart: always
    volumes:
      - ./flask:/app
    environment:
      - APP_NAME=FlaskApp
    expose:
      - 8080

  nginx:
    build: ./nginx
    volumes:
      - "./nginx/logs:/var/log/nginx"
    container_name: nginx
    restart: always
    ports:
      - "80:80"

    depends_on:
      - flask


### ./flask/Dockerfile ###
FROM python:3.7.2-stretch
WORKDIR /app
ADD . /app
RUN pip install --upgrade pip
RUN pip install flask uwsgi requests
CMD ["uwsgi", "wsgi.ini"]


### ./flask/main.py ###
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)


### ./flask/wsgi.ini ###
[uwsgi]
wsgi-file = main.py
callable = app
socket = :8080
processes = 4
threads = 2
master = true
chmod-socket = 660
vacuum = true
die-on-term = true


### ./nginx/Dockerfile #####
# Use the Nginx image
FROM nginx

# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

# Replace with our own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/


### ./nginx/nginx.conf #####
server {
    listen 80;
    # server_name 0.0.0.0; 
    location / {
        include uwsgi_params;
        uwsgi_pass flask:8080;
    }
}

########################################
### HTTPS ##############################
########################################

### docker-compose.yml ###############
services:
  flask:
    build: ./flask
    container_name: flask
    restart: always
    volumes:
      - ./flask:/app
    environment:
      - APP_NAME=FlaskApp
    expose:
      - 8080

  nginx:
    build: ./nginx
    volumes:
      - ./nginx/logs:/var/log/nginx
      - ./nginx/ssl:/etc/nginx/ssl
    container_name: nginx
    restart: always
    ports:
      - 80:80
      - 443:443
    depends_on:
      - flask


### ./nginx/Dockerfile #####
# Use the Nginx image
FROM nginx

# Remove the default nginx.conf
RUN mkdir /etc/nginx/ssl
RUN rm /etc/nginx/conf.d/default.conf

# Replace with our own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/

### ./nginx/nginx.conf #####
server {
    listen 80;
    # server_name 0.0.0.0; 
    location / {
        include uwsgi_params;
        uwsgi_pass flask:8080;
    }
}

server {
  listen 80 default_server;
  listen [::]:80 default_server;
  rewrite ^(.*) https://$host$1 permanent;
  # server_name 0.0.0.0; 
  # location / {
  #     include uwsgi_params;
  #     uwsgi_pass flask:8080;
  # }
}

server {
  listen 443 ssl default_server;
  listen [::]:443 ssl default_server;

  ssl_certificate /etc/nginx/ssl/cert.crt;
  ssl_certificate_key /etc/nginx/ssl/cert.key;

   # server_name 0.0.0.0; 
  location / {
      include uwsgi_params;
      uwsgi_pass flask:8080;
  }
}

+---nginx
|   |   Dockerfile
|   |   nginx.conf
|   |   
|   +---ssl
|       |   cert.crt
|       |   cert.key
|
+---flask
|   |   Dockerfile
|   |   main.py
|   |   wsgi.ini
|
|   docker-compose.yml

'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Docker ( ubuntu nginx uwsgi flask )"
MyCodeString = '''
###  Docker ubuntu nginx uwsgi flask ####
## 檔案: mainCode_docker

### Dockerfile ###############
FROM ubuntu

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata
RUN ln -sf /usr/share/zoneinfo/Asia/Taipei /etc/localtime

RUN echo "Asia/Taipei" > /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata
RUN echo "Asia/Taipei" > /etc/timezone

RUN apt-get -y install nginx

RUN mkdir /app
WORKDIR /app
COPY default   /etc/nginx/sites-available/
COPY main.py   /app
COPY wsgi.ini  /app
COPY startHttp /app

RUN apt-get -y install python3 python3-pip python3-tk python3-dev scrot libpq-dev iftop ufw

RUN pip install --upgrade pip
RUN python3 -m pip install flask requests psycopg2 uwsgi ldap3
# CMD ["uwsgi", "--ini wsgi.ini"]

# docker build -t ubuntuflask .


### main.py ###############
#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()


### wsgi.ini ###############
[uwsgi]
wsgi-file = main.py
callable = app

### 使用 http 協議 ###
# http= :8001   

### 使用 uwsgi 協議 ###
socket = :8001

processes = 4
threads = 2
master = true
chmod-socket = 660
vacuum = true
die-on-term = true    

### default ###############
server{
    listen  80;
    location /{
        ## 使用 http 協議
        # proxy_pass  http://127.0.0.1:8001;

        ## 用 uwsgi 協議
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:8001;
    }
}

### startHttp ###############
#!/bin/bash
service nginx restart
uwsgi --ini wsgi.ini

### docker-compose.yml ###############
services:
  web:
    image: ubuntuflask
    container_name: ubuntuflask
    restart: always
    volumes:
      - ./nginx:/app
      - ./nginx/logs:/var/log/nginx
    environment:
      - APP_NAME=FlaskApp
    ports:
      - "80:80"
    command: /app/startHttp

# nikto -h 192.168.5.111  ## web scan

'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Docker ( jitsi )"
MyCodeString = '''
###  Docker jitsi ####
## 檔案: mainCode_docker
git clone https://github.com/jitsi/docker-jitsi-meet &amp;&amp; cd docker-jitsi-meet

cp env.example .env
./gen-passwords.sh

mkdir -p ./jitsi-meet-cfg/{web/crontabs,web/letsencrypt,transcripts,prosody/config,prosody/prosody-plugins-custom,jicofo,jvb,jigasi,jibri}

docker-compose up -d

# keys 的位置 ~/docker-jitsi-meet/jitsi-meet-cfg/web/keys

# 修改 .env
.env
CONFIG=./jitsi-meet-cfg
HTTPS_PORT=443
TZ=Asia/Taipei
PUBLIC_URL=https://xxx.xxx.com
DOCKER_HOST_ADDRESS=192.168.xx.xx
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Docker ( ubuntu install flask postgres )"
MyCodeString = '''
###  Docker ubuntu install flask postgres ####
## 檔案: mainCode_docker
#### 建立 ubuntu/flask 的 Dockerfile 內容 ####

FROM ubuntu

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata

RUN apt-get -y install net-tools curl systemd php7.4-sqlite3 sqlite3 iputils-ping
RUN ln -sf /usr/share/zoneinfo/Asia/Taipei /etc/localtime

RUN echo "Asia/Taipei" > /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata
RUN echo "Asia/Taipei" > /etc/timezone

RUN apt-get -y install python3 python3-pip python3-tk python3-dev scrot libpq-dev
RUN python3 -m pip install flask requests psycopg2


#### 建制與匯出 ubuntu/flask ####
# docker build -t ubuntu/flask:1001 .
# docker save ubuntu/flask:1001 -o ubuntu-flask.tar


#### 匯入與啟動 ubuntu/flask ####
# docker load -i ubuntu-flask.tar 
# docker run -dit -p 8001:80 -v ./app:/app --name ubuntu-flask ubuntu/flask:1001 /app/main.py


#### 網頁 flask 的內容 ./app/main.py ####
#!/usr/bin/python3
import os
from flask import *

app = Flask(__name__)

@app.route( "/test" )
def test():
    return "test"

app.run(host='0.0.0.0', port=80, debug=True)

#### 使用 docker-compose.yml 啟動 ####
# vi docker-compose.yml
services:
  flask:
    image: ubuntu/flask
    container_name: flask
    restart: always
    ports:
      - 80:80
    volumes:
      - ./app:/app    
    command: /app/main.py

    depends_on:
      - flask_db

  flask_db:
    image: postgres:12.4
    container_name: flask_db
    restart: always
    environment: 
        - "TZ=Asia/Taipei"
        - "POSTGRES_DB=mydb"
        - POSTGRES_PASSWORD=12345678
    expose:
        - "5432"
    ports:
        - "5432:5432"
    volumes:
        - ./postgres:/var/lib/postgresql/data
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Docker ( gitlab )"
MyCodeString = '''
###  Docker gitlab ####
## 檔案: mainCode_docker
## 使用 docker run
sudo docker run --detach \
  --hostname gitlab.example.com \
  --publish 443:443 --publish 80:80 --publish 2022:22 \
  --name gitlab \
  --restart always \
  --volume /gitlab/config:/etc/gitlab:Z \
  --volume /gitlab/logs:/var/log/gitlab:Z \
  --volume /gitlab/data:/var/opt/gitlab:Z \
  gitlab/gitlab-ce:latest


## 使用 docker-compose.yml
version: '3.2'
services:
 
  gitlab:
    image: gitlab/gitlab-ce:latest
    hostname: gitlab.example.com
    container_name: gitlab
    restart: always
    volumes:
      - /gitlab/config:/etc/gitlab
      - /gitlab/logs:/var/log/gitlab
      - /gitlab/data:/var/opt/gitlab
    ports:
      - 443:443
      - 80:80


# 更改 root 密碼
# docker exec -it 容器名稱 bash

# 重設密碼
gitlab-rails console -e production
user = User.where(id: 1).first
user.password = '12345678'
user.password_confirmation = '12345678'
user.save
exit
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")





### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Docker ( postgresql pgadmin4 )"
MyCodeString = '''
###  Docker postgresql pgadmin4 ####
## 檔案: mainCode_docker
version: '3'
services:

  postgresql:
    image: postgres:12
    restart: always
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: 123456

    mem_limit: 1536MB
    mem_reservation: 1G
    volumes:
      - /docker/postgres:/var/lib/postgresql/data      
    ports:
      - "5432:5432"

  pgadmin4:
    image: dpage/pgadmin4
    restart: always
    depends_on:
      - postgresql
    ports:
      - "53603:53603"
      - "80:80"
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@abc.com
      PGADMIN_DEFAULT_PASSWORD: root1234
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Docker ( php mysql mysqladmin )"
MyCodeString = '''
###  Docker php mysql mysqladmin ####
## 檔案: mainCode_docker
#

# vi docker-compose.yml
version: '3'
services:
  web:
    image: php:7.0-apache
    restart: always
    ports:
      - 80:80
      - "443:443"
    volumes:
      - /docker/www:/var/www/html
    depends_on:
      - mysql      

  mysql:
    image: mysql:5.6
    restart: always
    ports:
      - "3306:3306"
    volumes:
      - /docker/mysql:/var/lib/mysql
    
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_DATABASE: test_db
      MYSQL_USER: user
      MYSQL_PASSWORD: pass

  phpmyadmin:
    restart: always
    depends_on:
      - mysql
    image: phpmyadmin/phpmyadmin
    container_name: phpmyadmin
    ports:
      - "8080:80"
    environment:
      PMA_HOST: mysql

$ docker-compose up -d
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Docker ( postgres )"
MyCodeString = '''
###  Docker postgres 安裝 ####
## 檔案: mainCode_docker
# vi docker-compose.yml

version: '3.7'
services:
    MyPgDB:
        image: postgres
        container_name: MyPgDB
        restart: always
        environment:
            - "TZ=Asia/Taipei"
            - "POSTGRES_DB=MyPgDB"
            - POSTGRES_PASSWORD=123456
        expose:
            - "5432"
        ports:
            - "5432:5432"
        volumes:
            - ./data:/var/lib/postgresql/data/


# docker-compose up -d
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Docker ( Container 之間的資料共享 - volumes )"
MyCodeString = '''
###  Docker 範例程式 ####
## 檔案: mainCode_docker

Container 之間的資料共享

啟動第一個 Container
docker run -it -v /data --name=container1 centos /bin/bash

啟動第二個 Container
docker run -it --volumes-from container1 --name=container2 centos /bin/bash

'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Docker ( 安裝 docker 範例 )"
MyCodeString = '''
###  安裝 docker 範例 ####
## 檔案: mainCode_docker

## https://docs.docker.com/engine/install/ubuntu/
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

## 安裝 docker-compose
## https://docs.docker.com/compose/install/

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# non root 執行 docker
# 建立 docker group , 如果已經有就不用
# sudo groupadd docker
# 將 my_username 帳號加上 docker 群組中
sudo usermod -G docker -a my_username
# 立刻更新
newgrp docker
# 重啟服務
sudo systemctl restart docker


## 安裝 portainer
## https://github.com/twtrubiks/docker-tutorial

docker search portainer
docker pull portainer/portainer
docker volume create portainer_data
docker run --name=portainer --restart=always -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer

## 設定 portainer
# 於左側框架點選 [Endpoints] 後，選擇 [local]。
# 於 [Endpoint details] 頁面中輸入 NAS Public IP，這是 Docker 部署 Container 的 Default IP。 

'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


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
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")




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

### 封裝 build 和 執行 run
docker build -t UbuntuPHP74 .
docker run -it --rm UbuntuPHP74 bash
docker run -dit --rm -p 80:80 -v /usr/local/docker/UbuntuPHP74/html:/var/www/html --name php UbuntuPHP74 startHttp

### with nginx + php
# apt install -y nginx php7.4 php7.4-fpm php7.4-cgi php7.4-common
# vi /etc/nginx/sites-available/default

server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
    index index.php index.html index.htm index.nginx-debian.html;	
	server_name _;

	location / {
		try_files $uri $uri/ =404;
	}

	location ~ \.php$ {
		include snippets/fastcgi-php.conf;
	#	# With php-fpm (or other unix sockets):
		fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
	#	# With php-cgi (or other tcp sockets):
	#	fastcgi_pass 127.0.0.1:9000;
	}
	location ~ /\.ht {
		deny all;
	}
}

'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Docker ( save load images 匯出匯入 )"
MyCodeString = '''
###  Docker save load images 匯出匯入 ####
### 檔案: Dockerfile

docker save -o <path for generated tar file> <image name>
docker load -i <path to image tar file>
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")

