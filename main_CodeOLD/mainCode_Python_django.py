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
# MyCodeTitle  = "RyanCode Python django ( 範例 )"
# MyCodeString = '''
# ###  Python django 範例程式 ####
# ### file: mainCode_Python_django
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)



# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python django ( 範例 )"
# MyCodeString = '''
# ###  Python django 範例程式 ####
# ### file: mainCode_Python_django
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)



# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python django ( 範例 )"
# MyCodeString = '''
# ###  Python django 範例程式 ####
# ### file: mainCode_Python_django
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)



# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python django ( 範例 )"
# MyCodeString = '''
# ###  Python django 範例程式 ####
# ### file: mainCode_Python_django
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python django ( 基本設定 )"
MyCodeString = '''
###  Python django 基本設定 ####
### file: mainCode_Python_django

## 基本設定 settings.py
LANGUAGE_CODE = 'zh-hant'
TIME_ZONE = 'Asia/Taipei'

# 創建一個專案
django-admin startproject HelloJango

## ???
python manage.py migrate

# 啟動服務
python manage.py runserver
python manage.py runserver 0.0.0.0:8000


## 建立一個 app
python manage.py startapp app

## 修改 HelloJango/settings.py
## 把它加入 INSTALLED_APPS：
INSTALLED_APPS = [
    ... ,
    ... ,
    'app',
]





## 修改 HelloJango/urls.py
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('',views.hello),
    path('admin/', admin.site.urls),
]


## 修改 app/views.py

from django.shortcuts import render
from django.http import HttpResponse

def hello(request):    
    return HttpResponse("My Test")



############################################
## 網頁放置 HelloJango/app/templates/home.html
############################################
## 建立 app/templates/home.html

## 修改 HelloJango/urls.py 的 urlpatterns 參數
urlpatterns = [
    ...
    path('home/' , views.home,name='home'),
]

## 修改 app/views.py
def home(request):
    return render(request,'home.html')




############################################
## 網頁放置 根目錄 HelloJango/templates/test.html
############################################

## 修改 HelloJango/settings.py 中的 TEMPLATES , 加入 BASE_DIR 根目錄的 templates 位置
'DIRS': [BASE_DIR, 'templates' ],

## 修改 HelloJango/urls.py 的 urlpatterns 參數
urlpatterns = [
    ...
    path('test/',views.test,name='test'),
]

## 修改 app/views.py
def test(request):
    return render(request,'test.html')



############################################
## 建立專案 app2 , http://127.0.0.1:8000/app2/index/
############################################
## 建立一個 app2
python manage.py startapp app2

## 修改 HelloJango/settings.py
## 把它加入 INSTALLED_APPS：
INSTALLED_APPS = [
    ... ,
    'app2',
]


## 修改 HelloJango/urls.py
from django.urls import path, include
urlpatterns = [
    ...
    path('app2/', include('app2.urls')),
]


## 加入 app2/urls.py
from django.contrib import admin
from django.urls import path
from app2 import views

urlpatterns = [
    path('index/', views.index),
]


## 加入 app2/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):    
    return HttpResponse("My app2")




############################################
## 建立專案 app2 , 建立 db
############################################
## 設定 databases 修改 app2/models
class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_age = models.IntegerField(default=1)

## 執行 makemigrations 建立 db
python manage.py makemigrations
python manage.py migrate


## 加入 app2/urls.py
urlpatterns = [
    ...
    path('addstudent/' , views.add_student),
    path('getstudent/' , views.get_student),
]

## 加入 app2/views.py
def add_student(request):
    student = Student()
    student.s_name = f"Albert{ random.randrange(100) }"
    student.save()
    return HttpResponse(f"Add Sucesses{student.s_name}")

def get_student(request):
    students = Student.objects.all()
    # for student in students:
    #     print(student.s_name)

    context = {
        "MyGame": "Play game" , 
        "students" : students
    }

    return render(request, 'student_list.html' , context=context)

## 根目錄 HelloJango/templates/student_list.html
<h1>Ubuntu</h1>
<h2>{{MyGame}}</h2>
<ul>
    {% for student in students %}
        <li>{{ student.s_name}}</li>
    {% endfor %}
</ul>

## 執行 python manage.py runserver

'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)









##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
