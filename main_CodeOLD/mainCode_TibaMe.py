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
# MyCodeTitle  = "RyanCode TibaMe class ( 範例 )"
# MyCodeString = '''
# ###  TibaMe class 範例程式 ####
# ### file: mainCode_TibaMe
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode TibaMe class ( 範例 )"
# MyCodeString = '''
# ###  TibaMe class 範例程式 ####
# ### file: mainCode_TibaMe
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode TibaMe class ( 範例 )"
# MyCodeString = '''
# ###  TibaMe class 範例程式 ####
# ### file: mainCode_TibaMe
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode TibaMe class ( 範例 )"
# MyCodeString = '''
# ###  TibaMe class 範例程式 ####
# ### file: mainCode_TibaMe
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode TibaMe class ( url )"
MyCodeString = '''
###  TibaMe class 範例程式 ####
### file: mainCode_TibaMe
shorturl.at/pzS39
https://drive.google.com/drive/folders/1k0xm58Z8VwHwsyqzfXfs6JRs_87ZkEMT
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode TibaMe 20200802 上課( tensorflow basic )"
MyCodeString = '''
###  TibaMe tensorflow basic ####
### file: mainCode_TibaMe

## 基本操作 ##################################
import tensorflow as tf
tf.reset_default_graph()

a = tf.constant(5, name="input_a")
b = tf.constant(3, name="input_b")
c = tf.multiply(a, b, name="mul_c")
d = tf.add(a, b, name="add_d")
e = tf.add(c, d, name="add_e")

with tf.Session() as sess:
    print(sess.run(e)) # output => 23

x = tf.constant([[1, 2],[3, 4]], name='x')
y = tf.constant([[5, 6],[7, 8]], name='y')

tf_sum = tf.add(x, y)
tf_sub = tf.subtract(x, y)
tf_mul = tf.multiply(x, y)
tf_div = tf.div(x,y)
tf_mod = tf.mod(x,y)
tf_neg = tf.negative(x)

with tf.Session() as sess:

    print("directly print x: {}\\n".format(x))
    print("directly print y: {}\\n".format(y))

    print("x: {}\\n".format(sess.run(x)))
    print("y: {}\\n".format(sess.run(y)))
    print("x+y: {}\\n".format(sess.run(tf_sum)))
    print("x-y: {}\\n".format(sess.run(tf_sub)))
    print("x*y: {}\\n".format(sess.run(tf_mul)))
    print("x/y: {}\\n".format(sess.run(tf_div)))
    print("x mod y: {}\\n".format(sess.run(tf_mod)))
    print("-x: {}\\n".format(sess.run(tf_neg)))

### constant ################################
import tensorflow as tf
tf.reset_default_graph()

matrix1 = tf.constant([[1, 2],[3, 4]], name='matrix1', dtype=tf.float32)
matrix2 = tf.constant([[5, 6],[7, 8]], name='matrix2', dtype=tf.float32)

product = tf.matmul(matrix1, matrix2)
inv = tf.matrix_inverse(matrix1)
trans = tf.matrix_transpose(matrix1)

with tf.Session() as sess: 
    print("product: {}\\n".format(sess.run(product)))
    print("inv: {}\\n".format(sess.run(inv)))
    print("trans: {}\\n".format(sess.run(trans)))

#### 變更型態 ################################
import tensorflow as tf
tf.reset_default_graph()

x_float32 = tf.constant([[1.1, 2.2],[3.3, 4.4]], dtype=tf.float32) # define float32 tensor
x_int = tf.cast(x_float32, tf.int32) #change type to int32

with tf.Session() as sess:
    print(x_float32)
    print(sess.run(x_float32))

    print(x_int)
    print(sess.run(x_int))
    
#### Variable ################################
import tensorflow as tf
tf.reset_default_graph()

x_constant1 = tf.constant([[1.1, 2.2],[3.3, 4.4]], dtype=tf.float32) # define float32 tensor
x_constant2 = tf.zeros([2,3])
x_constant3 = tf.random_normal([1,3], stddev=1)

x_variable1 = tf.Variable(tf.constant([[1.1, 2.2],[3.3, 4.4]], dtype=tf.float32))
x_variable2 = tf.Variable(tf.zeros([2,3]))
x_variable3 = tf.Variable(tf.random_normal([1,3], stddev=1))


w1= tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2= tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))
x_placeholder1 = tf.placeholder(tf.float32, shape=(3, 2), name="input")
a = tf.matmul(x_placeholder1, w1)
y = tf.matmul(a, w2)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print('this is constant:')
    print(sess.run(x_constant1))
    print(sess.run(x_constant2))
    print(sess.run(x_constant3))
    print('this is variable:')
    print(sess.run(x_variable1))
    print(sess.run(x_variable2))
    print(sess.run(x_variable3))
    
    print('y is:')
    print(sess.run(y, feed_dict={x_placeholder1: [[0.7,0.9],[0.1,0.4],[0.5,0.8]]}))

#### argmax ################################
import tensorflow as tf
tf.reset_default_graph()

test =tf.constant([[1.1, 2.2, 3.3],[4.5, 3.2, 2.1]], dtype=tf.float32)

reduce_sum = tf.reduce_sum(test)
reduce_mean = tf.reduce_mean(test)
arg_max = tf.argmax(test)
arg_min = tf.argmin(test)


with tf.Session() as sess:
    print(sess.run(reduce_sum))
    print(sess.run(reduce_mean))

    print(sess.run(arg_max))
    print(sess.run(arg_min))

####################################
import tensorflow as tf
tf.reset_default_graph()

a = tf.constant([[1.0, 2.0], [3.0, 4.0]], name='a')
b = tf.constant([[1.0, 1.0], [0.0, 1.0]], name='b')
c = tf.Variable(tf.random_normal([2,2], stddev=1), name='c')
d = tf.Variable(tf.random_normal([2,2], stddev=1), name='d')
e = tf.matmul(c, d, name='e')
f = tf.matmul(e,c) + d

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())    
    print('=================\\n')
    for v in tf.global_variables():
        print('{} with value \\n{}'.format(v.name, sess.run(v)))
    print('=================\\n')
    for v in tf.trainable_variables():
        print('{} with value \\n{}'.format(v.name, sess.run(v)))

#### unstack 矩陣分割 ################################
import tensorflow as tf
tf.reset_default_graph()

x = tf.constant([[0.7,0.9],[0.1,0.4],[0.5,0.8]], name='x')
axis0_x = tf.unstack(x, axis=0)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    x_, axis0_ = sess.run([x, axis0_x])
    print('before unstack......')
    print(x_)
    print('after unstack......')
    print(axis0_[0])
    print(axis0_[1])
    print(axis0_[2])

#### stack 矩陣合併 ################################
import tensorflow as tf
tf.reset_default_graph()

x = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]], name='x')
y = tf.constant([[1.0, 1.0], [0.0, 1.0], [1.0, 1.0]], name='y')

stacked_axis0_result = tf.stack([x,y], axis=0)
stacked_axis1_result = tf.stack([x,y], axis=1)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    stacked_axis0_result_, stacked_axis1_result_ = sess.run([stacked_axis0_result, stacked_axis1_result])
    print(stacked_axis0_result_)
    print(stacked_axis0_result_.shape)
    
    print(stacked_axis1_result_)
    print(stacked_axis1_result_.shape)

#### 激活函數 Activation Function ################################
import tensorflow as tf
tf.reset_default_graph()

a = tf.constant([-1.0, 2.0], name='a')
relu_out = tf.nn.relu(a)
sigmoid_out = tf.sigmoid(a)
tanh_out = tf.tanh(a)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    relu_out_, sigmoid_out_, tanh_out_ =  sess.run([relu_out, sigmoid_out, tanh_out])

    print('output of relu is\\n {} \\n'.format(relu_out_))
    print('output of sigmoid is\\n {} \\n'.format(sigmoid_out_))
    print('output of tanh is\\n {} \\n'.format(tanh_out_))
    
#### softmax cross_entropy with logits_v2 ################################
import tensorflow as tf
tf.reset_default_graph()

predict = tf.constant([-0.5, 1, 2], name='predict')
labels = tf.constant([1.0, 0.0, 0.0], name='labels')

cost1 = tf.nn.softmax_cross_entropy_with_logits_v2(logits=predict , labels=labels)
cost2 = tf.losses.mean_squared_error(predictions=predict, labels=labels) 

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    cost1_ =  sess.run(cost1)
    cost2_ =  sess.run(cost2)

    print('softmax with cross entropy is\\n {} \\n'.format(cost1_))
    print('mean square is\\n {} \\n'.format(cost2_))

#### 優化器 Optimizer ################################
import tensorflow as tf
tf.reset_default_graph()

learning_rate = 0.01
a = tf.constant(2.0)
b = tf.constant(1.0)
c = tf.constant(3.0)
x = tf.Variable(tf.constant(1.0), name='x')
y = a*x*x + b*x + c

optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(y)
#optimizer = tf.train.AdamOptimizer(learning_rate).minimize(y)
#optimizer = tf.train.RMSPropOptimizer(learning_rate).minimize(y)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for _ in range(1000):
        optimizer_ = sess.run(optimizer)
    x_ = sess.run(x)    
    print('when x = {}, y have min value'.format(x_))    

##### DNN ###############################

import tensorflow as tf
tf.reset_default_graph()

learning_rate = 0.01
a = tf.placeholder(tf.float32, shape=(1), name="input")
b = tf.constant(1.0)
c = tf.constant(3.0)
x = tf.Variable(tf.constant(1.0), name='x')
y = tf.add(a*x*x + b*x ,c , name='output')

optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(y)

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for _ in range(100):
        optimizer_ = sess.run(optimizer, feed_dict={a:[2]})
    x_ = sess.run(x)
    saver.save(sess, "Saved_model/model.ckpt")
    print('when x = {}, y have min value'.format(x_))  

#### Save and Restore Model ################################
import tensorflow as tf
tf.reset_default_graph()

learning_rate = 0.01
a = tf.placeholder(tf.float32, shape=(1), name="input")
b = tf.constant(1.0)
c = tf.constant(3.0)
x = tf.Variable(tf.constant(1.0), name='x')
y = tf.add(a*x*x + b*x ,c , name='output')

optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(y)

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver.restore(sess, "Saved_model/model.ckpt")
    print(sess.run(x))

#### Save and Restore Model ################################
import tensorflow as tf
tf.reset_default_graph()

saver = tf.train.import_meta_graph("Saved_model/model.ckpt.meta")
with tf.Session() as sess:
    saver.restore(sess, "Saved_model/model.ckpt")
    print(sess.run("x:0"))
    print(sess.run("output:0", feed_dict={"input:0":[2.0]}))

'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode TibaMe 20190922 上課 ( requests BeautifulSoup pandas )"
MyCodeString = '''

Ubuntu jupyter 基本安裝
sudo python3 -m pip install requests
sudo python3 -m pip install beautifulsoup4
sudo python3 -m pip install pandas
sudo python3 -m pip install jupyter
sudo python3 -m pip install jupyterlab
jupyter notebook &

老師位置 https://github.com/ywchiu/tibamepy

###  TibaMe 20190922 上課 範例1 ###########################################

import requests
from bs4 import BeautifulSoup
import pandas

url = 'https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007001010%2C2007002000&area=6001002023&order=1&asc=0&page=1&mode=s&jobsource=2018indexpoc'
headers = {
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
}

data = []

res = requests.get(url , headers = headers)

# soup = BeautifulSoup( res.text , 'lxml')
# soup = BeautifulSoup( res.text , 'xml' )
soup = BeautifulSoup( res.text , 'html.parser' )

for html in soup.select('article .b-block__left'):
    title = html.select_one('a.js-job-link').text.strip()
    name = html.select_one('li a').text.strip()
    jobs = html.select_one('p.job-list-item__info').text.strip()
    date = html.select_one('span.b-tit__date').text.strip()
    
    data.append( {
        '公司名稱'  : name,
        '職稱' : title,
        '內容'  : jobs,
        '日期'  : date,
    } )

pandas.DataFrame(data)

###  TibaMe 20190922 上課 範例2 ###########################################

import requests
url = 'https://www.thsrc.com.tw/tw/TimeTable/Search'

payload = {
'StartStationName':  '台北站',
'EndStationName':  '新竹站',
'SearchType': 'S',
'StartStation': '977abb69-413a-4ccf-a109-0272c24fd490',
'EndStation': 'a7a04c89-900b-4798-95a3-c01c455622f4',
'DepartueSearchDate': '2019/09/22',
'DepartueSearchTime': '18:30'    
}

res = requests.post(url, data = payload)

###  TibaMe 上課 範例3 ###########################################

import requests
url = 'https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybytime'
payload = {
'startStation': '0900-基隆',
'endStation': '0990-松山',
'transfer': 'ONE',
'rideDate': '2019/09/22',
'startOrEndTime': 'true',
'startTime': '00:00',
'endTime': '23:59',
'trainTypeList': 'ALL',
'query': '查詢'    
}
res = requests.post(url, data = payload)


###  TibaMe 上課 範例4 ###########################################

s = '<a href="link" data="qoo" abc="def"></a>'
s2 = BeautifulSoup(s,'lxml')
print(s2.select_one('a').get('data'))
print(s2.select_one('a').get('href'))
print(s2.select_one('a').get('abc'))

###  TibaMe 20190922 上課 flask 回傳 headers ###########################################

from flask import Flask,jsonify
from flask import request

app=Flask(__name__)

@app.route("/")
def getSalary():
	return jsonify({'data' :request.headers.get('User-Agent') })

if __name__=="__main__":
	app.run()




### END TibaMe 上課 範例 ###########################################

'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)










##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
