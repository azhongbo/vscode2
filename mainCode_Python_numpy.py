#!/usr/bin/python3
import sys


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python numpy ( np 範例 )"
# MyCodeString = '''
# ###  Python numpy np 範例程式 ####
# ### file: mainCode_Python_numpy
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python numpy ( np 範例 )"
# MyCodeString = '''
# ###  Python numpy np 範例程式 ####
# ### file: mainCode_Python_numpy
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python numpy ( np 範例 )"
# MyCodeString = '''
# ###  Python numpy np 範例程式 ####
# ### file: mainCode_Python_numpy
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python numpy ( np 範例 )"
# MyCodeString = '''
# ###  Python numpy np 範例程式 ####
# ### file: mainCode_Python_numpy
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python numpy ( np array 合併範例 )"
MyCodeString = '''
###  Python numpy np np array 合併範例 ####
### file: mainCode_Python_numpy
import numpy as np

nd1 = np.random.randint(0,150,size = (4,5))
nd2 = np.random.randint(0,150,size = (2,5))
nd3 = np.random.randint(0,150,size = (4,8))
display(nd1,nd2,nd3)

np.concatenate([nd1,nd3],axis = 1) ## 使用 np.concatenate() 水平合併
np.concatenate([nd1,nd2],axis = 0) ## 使用 np.concatenate() 垂直合併
nd5 = np.hstack((nd1,nd3))         ## 使用 np.hstack() 水平的列數增加
nd4 = np.vstack((nd1,nd2))         ## 使用 np.vstack() 垂直行數增多
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")






### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python numpy ( np.concatenate 合併圖片 )"
MyCodeString = '''
###  Python numpy np.concatenate 合併圖片 ####
### file: mainCode_Python_numpy

import numpy as np
from PIL import Image

## 使用 聯集 np.concatenate() 合併陣列
nd2 = np.random.randint(0,150,size = (4,5))
np.concatenate([nd2,nd2])


## 使用 聯集 np.concatenate() 合併圖片
cat = Image.open('cat.jpg')
cat_data = np.array(cat)

cat7 = cat_data[:,:230] ## 圖片取左邊 230px
plt.imshow(cat7)

cat8 = cat_data[:,470:,::-1] ## 圖片取右邊 470px
plt.imshow(cat8)

cat9 = np.concatenate([cat7,cat8],axis = 1) ## 合併
plt.imshow(cat9)

xxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python numpy ( np 和 matplotlib 圖片操作 )"
MyCodeString = '''
###  Python numpy np 和 matplotlib 圖片操作 ####
### file: mainCode_Python_numpy

import matplotlib.pyplot as plt
%matplotlib inline

cat = Image.open('cat.jpg')
cat_data = np.array(cat)

plt.imshow( cat_data ) # 顯示
plt.imshow( cat_data[::-1] ) #反轉
plt.imshow( cat_data[::-15,::-15] ) #馬賽克
plt.imshow( np.transpose(cat_data,axes = (1,0,2))  )  # 向左邊轉，行列调整 -- 高度 0、宽度 1、像素 2
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python numpy ( np 和 PIL 圖片操作 )"
MyCodeString = '''
###  Python numpy np 和 PIL 圖片操作 ####
### file: mainCode_Python_numpy

import numpy as np
from PIL import Image

cat = Image.open('cat.jpg')
cat_data = np.array(cat)

# 红绿蓝 0,1,2
# 绿红蓝 1,0,2
Image.fromarray( cat_data[:,:,::-1]     ) ## 轉藍色
Image.fromarray( cat_data[:,:,[1,0,2]]  ) ## 轉綠色
Image.fromarray( cat_data[:,:,0]        ) ## 轉灰階
Image.fromarray( cat_data[::5,::5]      ) ## resize
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python numpy ( np 基本範例 )"
MyCodeString = '''
###  Python numpy np 基本範例 ####
### file: mainCode_Python_numpy
import numpy as np

nd.sum() ## 總和
nd.var() ## 方差
nd.mean() ## 平均
nd.std() ## 標準差

## 搭配 DataFrame
pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))

## %timeit測試時間
%timeit np.arange(0,100000,1) 

## 建立list
l = [1,2,3,4,5,9,8,7,6]
nd = np.array(l)

l2 = [[1,3,5,7],[2,4,6,8]]
nd2 = np.array(l2)

#一維陣列建立
np.array([1, 2, 3, 4])

#二維陣列建立
np.array([(2.5, 1, 3, 4.5), (5, 6, 7, 8)], dtype = float)

#三維陣列建立
np.array([[(2.5, 1, 3, 4.5), (5, 6, 7, 8)], [(2.5, 1, 3, 4.5), (5, 6, 7, 8)]], dtype = float)

np.zeros((2, 3))               # 全部為 0  建立一個2x3全為0的陣列
np.ones((2, 3, 4))             # 全部為 1 建立一個2x3x4全為1的陣列
np.arange(1, 10, 2)            # 建立一個由1開始，不超過10，間隔值為2的均勻數值陣列
np.full((3,2), 8)              # 全部為指定數字  建立一個3x2全為8的陣列
np.linspace(0, 10, 5)          # 等差列數  建立一個0到10之間，均勻的5個數值陣列
np.eye(2)                      # 對角線陣列 建立一個5x5的單位矩陣

## 隨機建立
np.random.random((2,3))        # 建立一個2x3的隨機值矩陣
np.random.rand(4,2)            #  生成[0,1)之間的數據，包含0，不包含1 , shape: 4x2 
np.random.randn(2,4)           # 常態分佈
np.random.randint(1,9 ,size=5) # 1~9 隨機整數


## 常態分佈的擬合
np.random.normal(loc = 175,scale=10,size = 10000).round(2) ## 平均175 ,範圍10以內, 1000個
# loc：   此概率分佈的均值（對應著整個分佈的中心centre）
# scale： 此概率分佈的標準差（對應於分佈的寬度，scale越大越矮胖，scale越小，越瘦高）
# size：  輸出的shape，默認為None，只輸出一個值



###############
nd = np.random.randint(0,150,size = (4,5))  ## 產生 4x5 陣列
nd[1,1]     ## 取 1,1 的值
nd[2]       ## 取第2個列
nd[0:3]     ## 取 0~3 的列
nd[-2:]     ## 取倒數第2個之後
nd[0:3,0:3] ## 取 0~3 x 0~3 的資料
nd[::-1]    ## 反轉
nd[::2]     ## 兩個進行切片
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")














