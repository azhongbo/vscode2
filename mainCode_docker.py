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

