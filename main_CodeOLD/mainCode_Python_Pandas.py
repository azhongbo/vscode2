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
# MyCodeTitle  = "RyanCode Python Pandas ( 範例 )"
# MyCodeString = '''
# ###  Python Pandas 範例程式 ####
### file: mainCode_Python_Pandas

# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python Pandas ( 範例 )"
# MyCodeString = '''
# ###  Python Pandas 範例程式 ####
### file: mainCode_Python_Pandas

# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Python Pandas ( 範例 )"
# MyCodeString = '''
# ###  Python Pandas 範例程式 ####
### file: mainCode_Python_Pandas

# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python Pandas ( Apply Map ApplyMap )"
MyCodeString = '''
###  Python Pandas 範例程式 ####
## file: mainCode_Python_Pandas

### Map : 將函數套用到 Series 上每個元素 ###
def myFunc(myStr):
    return myStr.replace(" ","")

df['data'].map(myFunc) ## 使用 function
df['data'].map( lambda e: e.replace(" ","") ) ## 使用匿名函數


### Apply : 將函數套用到 DataFrame 上的行與列 ###
df = pd.DataFrame( [[10,20,30],[40,50,60],[70,80,90]] , columns = ['First','Second','Third'] )
df.apply( lambda e: e.max() - e.min() , axis=1 )  # 行 axis=0   列 axis=1


## ApplyMap : 將函數套用到 DataFrame 上每個元素
df.applymap( lambda e: '-' if pandas.isnull(e) else e )  ## 將缺失值 Nan 換成 -

'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)







### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python Pandas ( DataFrame 操作 )"
MyCodeString = '''
###  Python Pandas DataFrame 操作 ####
## file: mainCode_Python_Pandas

import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

## 建立 DataFrame
df = DataFrame(data = {'Python':np.random.randint(0,150,size =5 ),
                       'Math':np.random.randint(0,150,size = 5),
                       'En':np.random.randint(0,150,size = 5)},
               index = list('ABCDE'))

df2 = DataFrame(data = np.random.randint(0,150,size = (10,4)),
                index = list('ABCDEFHIJK'),
                columns=['Python','Math','En','Physic'])

## 讀取 csv / excel 建立 DataFrame
df3 = pd.read_csv('data.txt')
df4 = df3.rename(mapper = {'Unnamed: 0':'index'},axis = 1) ## 重新密命名第一行
df4.set_index(keys = 'index') ## 設定 index

df2.to_csv('data2.csv')     ## 檔案輸出 
df2.to_excel('data2.xlsx')  ## 檔案輸出 

## 顯示操作
df.values
df.index
df.shape
df.dtypes

df2 - 10       ## 所有資料 -10
df2.pow(2)     ## 所有資料 平方
df2.describe() ## 查看數據統計特徵，是 DataFrame 類型，只顯示能統計的列
df2.count()    ## 返回每一列中的非空值的個數
df2.sum()      ## 返回每一列的和，無法計算返回空，下同
df2.max()      ## 返回每一列的最大值
df2.min()      ## 返回每一列的最小值
df2.argmax()   ## 返回最大值所在的自動索引位置
df2.argmin()   ## 返回最小值所在的自動索引位置
df2.idxmax()   ## 返回最大值所在的自定義索引位置
df2.idxmin()   ## 返回最小值所在的自定義索引位置
df2.mean()     ## 返回每一列的均值
df2.median()   ## 返回每一列的中位數
df2.var()      ## 返回每一列的方差
df2.std()      ## 返回每一列的標準差
df2.isnull()   ## 檢查 df 中空值，NaN 為 True，否則 False，返回一個布爾數組
df2.notnull()  ## 檢查 df 中空值，非 NaN 為 True，否則 False，返回一個布爾數組
df2.sum(numeric_only=True) # numeric_only=True 代表只計算數字型元素，下同

## 列出某一行
df2.Python
df2['Math']
df2[['Math','En']]
df2.iloc[:,1:3]

## 列出某一列
df2.loc['A']
df2.loc[['A','C']]
df2.iloc[[3,5]]
df2['A':'F']
df2.iloc[0:5]

## 顯示某一個行列的值
df2['Math']['C'] 
df2.loc['C']['Python']
df2.loc['B','En']


df1 = DataFrame(np.random.randint(0,150,size = (5,3)),index = list('ABCDE')  ,columns=['Python','Math','En'] )
df2 = DataFrame(np.random.randint(0,150,size = (6,3)),index = list('ABCDEF') ,columns=['Python','Math','En'] )

df3 = df1 + df2                  ## 所有欄位內的資料相加,因行數不同，會出現空值
df5 = df1.add(df2,fill_value=0)  ## 所有欄位內的資料相加,因行數不同，補0後相加，不會出現空值

df3.loc['A':'E']= df3.loc['A':'E']/2  ## A~E所有行列資料 除2 放回原來欄位
s1 = df1.loc['A'] # 顯示列資料

s1 = df1.loc['A']

'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)





### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python Pandas ( Series 操作 )"
MyCodeString = '''
###  Python Pandas Series 操作 ####
## file: mainCode_Python_Pandas

import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt ## 繪圖視覺工具

s  = Series(data = np.random.randint(0,150,size = 10),index = list('abcdefhijk'),name = 'Python')
s.name = 'Math'    ## 更改名稱
s.astype(np.uint8) ## 變更型態

s.index  ## 顯示標籤
s.values ## 顯示值
s.head() ## 列出前5筆
s.tail() ## 列出後5筆

## 各種顯示索引方式
s['d']
s[['d','e','e','e','d']]
s[0]
s['a':'f']
s['a':'fjsljflsjf']
s[::2]
s.loc['a':'h']
s.loc[::-2]
s.iloc[0:3]
s.iloc[::3]
s.iloc[2]
s.loc['a']

## 指定空值
s[['d','i']]= np.NaN

## 找到空值
cond = s.isnull()
s[cond]

## 篩選非空值
cond = s.notnull()
s[cond]

## 加上值
s + 10 ##所有值加 10
s3 = s.add(10,fill_value=0) ## 空值給0 , 然後加10

s.mean()
s.median()
s.max()
s.std()
s.pow(2)
s.var()
s.value_counts() ## 各個值的統計數量

## 統計副檔名 的數量
li = ['xxxx.mp3','sfsa.wav','xfjs.mp3','fssfs.als','sfsjeio.ps','sfjsljfs.als']
def count_suffix(li):
    return Series([l.split('.')[-1] for l in li]).value_counts()[:2]
count_suffix(li)

## 合併 Series，因長度不同，合併後 會有空值
s2 = Series({ 'A':144 , 'B':137 , 'C':125 ,'D':99 })
s3 = Series({ 'A':88  , 'B':124 , 'C':67          })
s2 + s3

## 合併 Series，因長度不同，合併後 不會有空值
s2.add(s3,fill_value=0)

'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)







### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python Pandas 591 ( 範例 )"
MyCodeString = '''
###  Python Pandas 591 範例程式 ####
### file: mainCode_Python_Pandas

#### 抓網頁 #####

import requests
import pandas as pd
from bs4 import BeautifulSoup
rs = requests.session()
res = rs.get('https://rent.591.com.tw/?kind=1&region=1&section=5')
soup = BeautifulSoup(res.text, 'lxml')
token = soup.select_one('meta[name="csrf-token"]').get('content')
# print(token)

headers = {
'X-CSRF-TOKEN': token,
'X-Requested-With': 'XMLHttpRequest'    
}
res2 = rs.get('https://rent.591.com.tw/home/search/rsList?is_new_list=1&type=1&kind=1&searchtype=1&region=1&section=5&firstRow=30&totalRows=843', headers = headers)

jd = res2.json()
df = pd.DataFrame( jd['data']['data'] )

# df = pd.read_csv('https://raw.githubusercontent.com/ywchiu/tibamepy/master/data/rent_591_sample2.csv',index_col=0)

#### 開始處理 #####


df['search_date'] = pd.to_datetime( df['search_date'], format = '%Y-%m-%d' )

# df[ df['search_date'] >= '2017-05-04' ].head()
# df[ df['building_use'].isnull() ]


df2 = df[ df['building_use'].notnull() ] # 把空值取出

# 將 building_use 欄位切成兩個欄位 btype buse
df2['btype'] = df2['building_use'].map( lambda e: e.split('/')[0] )
df2['buse']  = df2['building_use'].map( lambda e: e.split('/')[1] )



# df2['btype'].unique()

btype = pd.get_dummies( df2['btype'] )  ### dummy variable , one hot
df2 = pd.concat( [df2,btype] , axis = 1 ) ## 合併

df2.drop( 'building_use' , axis = 1 , inplace=True  )


df2['price'] = df2['price'].map(lambda e: int(e.replace('元/月', '').replace(',','')))

df3 = df2.pivot_table(index='btype'
, columns='buse', values='price', aggfunc='mean')

#### 資料庫 #####

import sqlite3 as lite
con = lite.connect('test.sqlite')
cur = con.cursor()
cur.execute('SELECT SQLITE_VERSION();')
data = cur.fetchone()
print(data)
con.close()

import sqlite3 as lite
with lite.connect("test.sqlite") as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS PhoneAddress")
    cur.execute("CREATE TABLE PhoneAddress(phone CHAR(10) PRIMARY KEY, address TEXT, name TEXT unique, age INT NOT NULL)")
    cur.execute("INSERT INTO PhoneAddress VALUES('0912173381','United State','Jhon Doe',53)")
    cur.execute("INSERT INTO PhoneAddress VALUES('0928375018','Tokyo Japan','MuMu Cat',6)")
    cur.execute("INSERT INTO PhoneAddress VALUES('0957209108','Taipei','Richard',29)")
    cur.execute("SELECT phone,address FROM PhoneAddress")
    data = cur.fetchall()
    for rec in data:
        print(rec[0], rec[1])
        
        
import sqlite3 as lite
with lite.connect("test.sqlite") as con:
    cur = con.cursor()
    cur.execute("SELECT phone,address FROM PhoneAddress")
    data = cur.fetchone()
    print(data)
    data = cur.fetchall()
    print(data)


'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python Pandas map 虛擬變量 ( 範例 )"
MyCodeString = '''
###  Python Pandas map 虛擬變量 ####
### file: mainCode_Python_Pandas

## 將 Sex 欄位 map 成 Sex_num 欄位 , 值為 female時為0 值為 male 時為1
train['Sex_num'] = train.Sex.map({ 'female':0 , 'male':1 })

#顯示 Sex, Sex_num
train.loc[0:4 , ['Sex','Sex_num'] ]
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python Pandas ( for 迴圈 )"
MyCodeString = '''
###  Python Pandas for 迴圈 ####
for index,row in df.iterrows():
    print( row['aa'] , row['bb'] )
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python Pandas ( 讀取 Dict List  )"
MyCodeString = '''
###  Python Pandas from Dict List ####
### file: mainCode_Python_Pandas

import pandas as pd

# from CSV Excel
df = pd.read_csv("weather_data.csv")
df = pd.read_excel("weather_data.xlsx","Sheet1")

# 讀取 Dict (字典)
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'windspeed': [6,7,2],
    'event': ['Rain', 'Sunny', 'Snow']
}
df = pd.DataFrame(weather_data)

# 讀取 List
weather_data = [
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
]
df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])

# 讀取 List
weather_data = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'},    
]
df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python Pandas ( Handle Missing Data 缺失值 )"
MyCodeString = '''
###  Python Pandas Handle Missing Data 缺失值 ####
### file: mainCode_Python_Pandas

# 所有欄位一次填滿 
new_df = df.fillna(0)  #所有 na 填寫 0
new_df = df.fillna(method="ffill") #所有 na 抄寫上一筆資料
new_df = df.fillna(method="bfill") #所有 na 抄寫下一筆資料
new_df = df.fillna(method="bfill", axis="columns") # 左右欄位填滿 axis is either "index" or "columns" 
new_df = df.fillna(method="ffill",limit=1) ＃ 抄寫 1次

new_df = df.dropna()  #每筆內 只要有一欄是 na 就刪除
new_df = df.dropna(how='all') #每筆內，所有欄位都是 na 才刪除
new_df = df.dropna(thresh=1) # 比如 axis=0，thresh=10：標識如果該行中非缺失值的數量小於10，將刪除改行

## 使用日期 range 設定填滿 reindex
dt = pd.date_range("01-01-2017","01-11-2017")
idx = pd.DatetimeIndex(dt)
df.reindex(idx)

# 多筆欄位填滿 na 值
# col1 欄位1 將 na 填上 0
# col2 欄位1 將 na 填上 0
# col3 欄位1 將 na 填上 'No Event'
new_df = df.fillna({
        'col1': 0,
        'col2': 0,
        'col3': 'No Event'
    })
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)



### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python Pandas ( map apply applymap )"
MyCodeString = '''
###  Python Pandas map apply applymap ####
### file: mainCode_Python_Pandas

import pandas as pd
import numpy as np

### map 的用法 ###
df['price'].map(normalizePrice).head()
df['price'].map(lambda ele: int(ele.replace('元/月', '').replace(',', ''))).head()

### apply 的用法 ###
df = pd.DataFrame([
[60,70,50],
[80,79,68],
[63,66,82]], 
columns = ['First', 'Second', 'Third'])
df.apply(lambda e: e.max()-e.min(), axis = 0)  ## 每一個 row
df.apply(lambda e: e.max()-e.min(), axis = 1)  ## 每一個 column

### applymap 的用法 ###
df2 = pd.DataFrame([
['frank', 'M', np.nan], 
['mary', np.nan, np.nan], 
['tom' , 'M', 35], 
['ted' , 'M', 33], 
['jean' , np.nan, 21], 
['lisa', 'F', 20]])
df2.columns = ['name', 'gender', 'age']

df2.applymap(lambda e: '-' if pd.isnull(e) else e)  ## 如果空值，回傳 '-' 這個值
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python Pandas ( merge 合併範例 )"
MyCodeString = '''
###  Python Pandas merge 合併範例 ####
### file: mainCode_Python_Pandas

import pandas as pd

names = pd.DataFrame( [ ['1','User1' ],
                        ['2','User2' ],
                        ['3','User3' ]  ] )
names.columns = ['id','Name']

dep = pd.DataFrame( [ ['2' , 'IT'    ],
                      ['3' , 'Sales' ],
                      ['4' , 'HR'    ]  ] )
dep.columns = ['id','DEP']

pd.merge( names , dep , on = 'id' , how='outer' ).fillna('') # 左右全數出來
pd.merge( names , dep , on = 'id' , how='inner' ).fillna('') # 兩邊都有才出來
pd.merge( names , dep , on = 'id' , how='left'  ).fillna('') # 依照左邊
pd.merge( names , dep , on = 'id' , how='right' ).fillna('') # 依照右邊
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python Pandas ( 資料比對 isin contains  )"
MyCodeString = '''
###  Python Pandas 資料比對 isin contains ####
### file: mainCode_Python_Pandas

import pandas as pd

################################################
df = pd.DataFrame([ ['frank', 'M' , 29 ] , 
                    ['mary' , 'F' , 23 ] , 
                    ['tom'  , 'M' , 35 ] ,
                    ['ted'  , 'M' , 33 ] , 
                    ['jean' , 'F' , 21 ] , 
                    ['lisa' , 'F' , 20 ] ])
df.columns=['name', 'gender', 'age']
################################################
df = pd.DataFrame([ {'a': 1 , 'b': 2 },
                    {'a': 3 , 'c': 4 } ])

df = pd.DataFrame([
{'name':'frank' , 'gender':'M' , 'age':29} , 
{'name':'mary'  , 'gender':'F' , 'age':23} , 
{'name':'tom'   , 'gender':'M' , 'age':35} , 
{'name':'ted'   , 'gender':'M' , 'age':33} , 
{'name':'jean'  , 'gender':'F' , 'age':21} , 
{'name':'lisa'  , 'gender':'F' , 'age':20}  ])
################################################
emp = pd.DataFrame({
    'name' :['小美','小花','小明','小高','小王'] ,
    'age'  :[ 33,36,30,47,28] ,
    'dep'  :['資訊','會計','會計','人事','資訊'] ,
    'title':['資深工程師','資深主任','主任','經理','工程師'] ,
    'location':['2F-1R','3F-2R','1F-4R','1F-1R','3F-1R']
})
################################################
emp[ emp['title'].str.contains('主任|工程師') ]  ## like 搜尋
emp[ emp['dep'].isin(['會計','人事']) ]          ## 一般搜尋
emp[ emp['age'] < 35 ]                          ## 比對數值
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Python Pandas ( 資料分割 re extract 正規表示法 )"
MyCodeString = '''
###  Python Pandas 資料分割 re extract 正規表示法 ####
### file: mainCode_Python_Pandas


###############################
map = pd.DataFrame({
    'name'    :['小美','小花','小明','小高','小王'] ,
    'location':['2F-1R','3F-2R','1F-4R','1F-1R','3F-1R']
})

map[['floor','room']] = emp['location'].str.extract('(\d+[F])-(\d[R])')  ##使用正規表示法分割
###############################
df = pd.DataFrame({
    'name' :['小美','小花','小明','小高','小王'] ,    
    'room' :['透天厝/獨立套房','透天厝/獨立套房','電梯大樓/分租套房','透天厝/獨立套房','透天厝/分租套房'] 
})

df[['a','b']] = df['room'].str.extract('(.+[厝大樓])/(.+[房])')  ##使用正規表示法分割
###############################
df = pd.DataFrame({
    'name'    :['小美','小花','小明','小高','小王'] ,    
    'address' :['高雄市湖內區民生街','新北市蘆洲區長安街','新北市永和區中山路一段','屏東縣潮州鎮六合路','桃園市觀音區四維路'] 
})

df[['a','b','c']] = df['address'].str.extract('(.+[市縣])(.+[區鎮鄉市])(.+[街路村])')  ##使用正規表示法分割
###############################
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)









##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
