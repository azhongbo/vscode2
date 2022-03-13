#!/usr/bin/python3
import sys


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode AI( 範例 )"
# MyCodeString = '''
# ###  Python AI ####
# ### file: mainCode_ai
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode AI( 範例 )"
# MyCodeString = '''
# ###  Python AI ####
# ### file: mainCode_ai
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode AI( 範例 )"
# MyCodeString = '''
# ###  Python AI ####
# ### file: mainCode_ai
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode AI( NVIDIA GPU )"
MyCodeString = '''
###  Python AI ####
### file: mainCode_ai

如何選用適合自己訓練深度學習使用的 GPU?

這篇文章深入研究實測了各種 GPU，並根據不同的需求，為大家整理如何選用適合自己訓練深度學習使用的 GPU！
　　
重點整理
NVIDIA RTX 2080 Ti 運算速度快達到 GTX 1080 Ti 的兩倍（0.75 vs 0.4）

* 目前最好的 GPU：RTX 2080 Ti
* 成本效益高但貴的 GPU：RTX 2080、GTX 1080
* 成本效益高且便宜的 GPU：GTX 1070、GTX 1070 Ti、GTX 1060
* 用於超過 250 GB的資料集：RTX 2080 Ti or RTX 2080
* 只有一點錢的話：GTX 1060 (6GB)
* 幾乎沒什麼錢：GTX 1050 Ti (4GB) or CPU + AWS/TPU
* 打 Kaggle：GTX 1060 (6GB) 測試、AWS 做最後訓練
* 有競爭力的電腦視覺研究人員：GTX 2080 Ti，2019 年升級到 RTX Titan
* 研究人員：RTX 2080 Ti or GTX 10XX 到 RTX Titan
* 剛起步學習深度學習 (認真的)：從 GTX 1060 (6GB) 開始，或便宜的 GTX 1070/GTX 1070 Ti
* 只想試玩看看深度學習：GTX 1050 Ti (4或2GB)
註：作者文中的 RTX 2080/2080 Ti 是估算出來的值，這個月出貨後作者才會再更新這兩張 GPU 的實際數字。

https://timdettmers.com/2019/04/03/which-gpu-for-deep-learning/
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode AI( Keras 02.1 Iris 鳶尾花分類 )"
MyCodeString = '''
###  Python AI Keras 非線性回歸 ####
### file: mainCode_ai
import keras
from keras import layers
import numpy as np
import matplotlib.pyplot as plt
from keras.optimizers import  SGD
%matplotlib inline
import pandas as pd


## 讀取 Iris 資料
from sklearn.datasets import load_iris
iris = load_iris()

x =iris.data
y =iris.target

## 建立模型
model = keras.Sequential()
model.add(layers.Dense(units=3, input_dim=4, activation='softmax')) ## 輸出3層 , input_dim輸入4層 , 輸出10
model.summary() # 顯示模型

## 編譯 & 訓練
## 損失函數 sparse_categorical_crossentropy , 優化器 adam
model.compile( optimizer = 'adam', loss='sparse_categorical_crossentropy' , metrics=['acc'])  
model.fit( x,y ,epochs=1000)  # 訓練模型

## 繪製loss和acc變化曲線
plt.plot(range(300),history.history.get('loss'))
plt.plot(range(300),history.history.get('acc'))

## 測試一次
cost = model.evaluate(x, y, batch_size=40) #測試一遍
print('test cost:', cost)


## 繪製圖形
plt.figure(2, figsize=(8, 6))
plt.clf()

x_min, x_max = x[:, 0].min() - .5, x[:, 0].max() + .5
y_min, y_max = x[:, 1].min() - .5, x[:, 1].max() + .5

# Plot the training points
plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.Set1, edgecolor='k')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")





### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode AI( Keras 01.2 非線性回歸 )"
MyCodeString = '''
###  Python AI Keras 非線性回歸 ####
### file: mainCode_ai
import keras
from keras import layers
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

## 建立非線性函式
np.random.seed(0)
x=np.linspace(-0.5,0.5,200)
noise=np.random.normal(0,0.02,x.shape)
y=np.square(x)+noise

## 建立模型
model = keras.Sequential() 
model.add( layers.Dense(units=10,input_dim=1,activation='tanh') ) ## 輸出1層  , input_dim輸入1層 , 輸出10
model.add( layers.Dense(units=1,input_dim=10,activation='tanh') ) ## 輸出1層  , input_dim輸入10層 , 輸出1
model.summary()  # 顯示模型

## 編譯 & 訓練
model.compile( optimizer = 'adam', loss='mse')  ## 損失函數 Mean square error , 優化器 adam
model.fit( x,y ,epochs=1000)  # 訓練模型

## 繪製圖形
plt.scatter(x,y , c='r')
plt.plot(x,model.predict(x))

## 預測結果
model.predict(x)
model.predict([150]) ## 預測 第150個

## 測試一次
cost = model.evaluate(x, y, batch_size=40) #測試一遍
print('test cost:', cost)
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode AI( Keras 01.1 線性回歸 )"
MyCodeString = '''
###  Python AI Keras 線性回歸 ####
### file: mainCode_ai
import keras
from keras import layers
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

## 建立線性函式
x = np.linspace(0,100,30)
y = 3*x +7 + np.random.randn(30)

## 建立模型
model = keras.Sequential() 
model.add( layers.Dense(1, input_dim=1)  )  ## 輸出1層  , input_dim輸入1層
model.summary()  # 顯示模型

## 編譯 & 訓練
model.compile( optimizer = 'adam', loss='mse')  ## 損失函數 Mean square error , 優化器 adam
model.fit( x,y ,epochs=1000)  # 訓練模型

## 繪製圖形
plt.scatter(x,y , c='r')
plt.plot(x,model.predict(x))

## 預測結果
model.predict(x)
model.predict([150]) ## 預測 第150個

## 測試一次
cost = model.evaluate(x, y, batch_size=40) #測試一遍
print('test cost:', cost)
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode AI( Anaconda 建立環境 )"
MyCodeString = '''
###  Python AI Anaconda 建立環境 ####
### file: mainCode_ai

指令
conda create --name MyTest python=3.7
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode AI( Keras 03.1 mnist )"
MyCodeString = '''
###  Python 範例 ####
### file: mainCode_ai

from keras.datasets import mnist
from keras.utils import np_utils
import matplotlib.pyplot as plt

## copy mnist.npz 
!IF NOT EXIST %USERPROFILE%\.keras\datasets md %USERPROFILE%\.keras\datasets
!copy mnist.npz %USERPROFILE%\.keras\datasets /y

## 下載 mnist 資料
(train_feature,train_label) , (test_feature,test_label) = mnist.load_data()

# 顯示訓練資料長度
print( len(train_feature) , len(train_label) )

# 訓練資料是 60000 個 28x28 大小的單色圖片檔案，使用 shape 查看維度
print( train_feature.shape )

## 顯示 train_feature 圖片 ###
def show_image(image):
    fig = plt.gcf()
    fig.set_size_inches(2,2) # 數字圖片大小
    plt.imshow( image , cmap='binary') # 黑白顯示
    plt.show()

show_image( train_feature[11] )

### 開始資料預處理 - 轉換成一維向量 ###
# 以 reshape 將 28x28 的數字圖片  轉換為 784 一維向量
train_feature_vector = train_feature.reshape( len(train_feature) , 784 ).astype('float32')
test_feature_vector  = test_feature.reshape(  len(test_feature)  , 784 ).astype('float32')

# 以 shape 查看數字圖片屬性，已經轉換為  784 一維向量
#print(train_feature_vector.shape)

## 顯示 第一筆 資料內容
#print(train_feature_vector[0])

### 標準化 ###
# 將 一維向量 /255  得到 0~1 之間得浮點數，稱作標準化
# 可以提高模型預測準確度
train_feature_normalize = train_feature_vector / 255.0
test_feature_normalize  = test_feature_vector  / 255.0

### Label 資料預處理 - one hot  ###
## 將 Label 編碼成只有一個為1 其餘為0 ，增加模型效率
train_label_onehot = np_utils.to_categorical(train_label)
test_label_onehot = np_utils.to_categorical(train_label)

print(train_label[0:5])
print(train_label_onehot[0:5])

### 建立 Sequential 模型 ###
from keras.models import Sequential
model = Sequential()

### 建立 輸入層&隱藏層 ###
from keras.layers import Dense
model.add( Dense( units=256,
                  input_dim=784,
                  kernel_initializer='normal',
                  activation='relu' ))

### 建立輸出層 ###
model.add(Dense(units=10,
                kernel_initializer='normal',
                activation='softmax'))

### 訓練模型 ###
model.compile(loss='categorical_crossentropy',
              optimizer='adam',metrics=['accuracy'])

### 進行訓練 ###
train_history = model.fit( x=train_feature_normalize,
                          y=train_label_onehot,validation_split=0.2,
                          epochs=10, batch_size=200, verbose=2)


### 評估準確率 ###
scores = model.evaluate( test_feature_normalize, test_label_onehot)
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode AI ( 三角函數 )"
MyCodeString = '''
###  Python 三角函數 ####
### file: mainCode_ai

# python3 -m pip install matplotlib
# python3 -m pip install pandas

from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np

myfont = FontProperties(fname=r'/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc')

# 畫直線
plt.plot([0,1],[0,2])
plt.plot([5,10],[6,20])



# 畫拋物線
x = np.arange(2,10)
y = x ** 2
plt.plot(x,y)

plt.show()



x=[1,2,3,4,5]
y=[3,6,7,9,2]
 
fig,ax=plt.subplots(1,1)
ax.plot(x,y,label='trend')
ax.set_title('title test',fontsize=12,color='r')
plt.show()



plt.plot([0, 2], [0, 2])
plt.text(0.5, 1, 'tt 我的測試',fontproperties=myfont)
plt.show()


plt 
myfont = FontProperties(fname=r'/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc')

plt.plot((1,2,3),(4,3,1)) 
plt.title("聲量圖",fontproperties=myfont) 
plt.ylabel("文章數量",fontproperties=myfont) 
plt.xlabel("時間",fontproperties=myfont)  
plt.show()

'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


