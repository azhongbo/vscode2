#!/usr/bin/python3
import sys


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Tensorflow Basic ( xxxx )"
# MyCodeString = '''
# ###  Tensorflow xxxx ####
# ### file: mainCode_tf_basic
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Tensorflow Basic ( xxxx )"
# MyCodeString = '''
# ###  Tensorflow xxxx ####
# ### file: mainCode_tf_basic
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")






### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Tensorflow Basic ( eager mode 快速模式 )"
MyCodeString = '''
###  Tensorflow eager mode 快速模式 ####
### file: mainCode_tf_basic

from __future__ import absolute_import, division, print_function
import numpy as np
import tensorflow as tf

# Set Eager API
print("Setting Eager mode...")
tf.enable_eager_execution()
tfe = tf.contrib.eager

'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Tensorflow Basic ( Neural Network Playground )"
MyCodeString = '''
###  Tensorflow Neural Network Playground ####
### file: mainCode_tf_basic
深度 | 谷歌官方指南：如何通過玩 TensorFlow Playground 來理解神經網絡
A Neural Network Playground
https://playground.tensorflow.org/
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Tensorflow Basic ( Save/Restore )"
MyCodeString = '''
###  Tensorflow Save/Restore ####
### file: mainCode_tf_basic

##### Save ############################################################################
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

##### Restore method 1 ############################################################################
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

##### Restore method 2 ############################################################################
import tensorflow as tf
tf.reset_default_graph()

saver = tf.train.import_meta_graph("Saved_model/model.ckpt.meta")
with tf.Session() as sess:
    saver.restore(sess, "Saved_model/model.ckpt")
    print(sess.run("x:0"))
    print(sess.run("output:0", feed_dict={"input:0":[2.0]}))

'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Tensorflow Basic ( 掃描目錄照片 to train_data )"
MyCodeString = '''
###  Tensorflow 掃描目錄照片 to train_data ####
### file: mainCode_tf_basic
import numpy as np
from os import listdir
from random import shuffle
from PIL import Image

def preprocess_to_data_file( all_Folders , ratio=0.8):

    total_list = [] 

    ## 掃描 所有目錄 
    with open('total_data.txt', 'w') as f:
        for index, data_Path in enumerate(all_Folders):
            for filename in listdir(data_Path):
                f.write( f"{all_Folders[index]}/{filename.replace(' ','')} {index}\\n"  )
                total_list.append( all_Folders[index]+'/'+filename.replace(' ','')+' '+str(index))
                
    ## 洗牌 total_list
    shuffle(total_list)

    ## 80% 寫入 train_data.txt
    with open('train_data.txt', 'w') as f:
        for i in total_list[:int(ratio*len(total_list))]:
            f.write(i+'\\n')

    ## 20% 寫入 train_data.txt
    with open('test_data.txt', 'w') as f:
        for i in total_list[int(ratio*len(total_list)):]:
            f.write(i+'\\n')
            
image_path = ["./cat_dog/cat", "./cat_dog/dog"]
preprocess_to_data_file(image_path, 0.8)
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Tensorflow Basic ( one hot / batch 批次取得 )"
MyCodeString = '''
###  Tensorflow one hot / batch 批次取得 ####
### file: mainCode_tf_basic

# one hot 方法一
xlabel1 = ( np.eye(10)[xlabel] )

# one hot 方法二
def one_hot(values):
    n_values = np.max(values) + 1
    return np.eye(n_values)[values]

# batch 批次取得 方法

batch_size = 5000 ## 每次訓練比數
data_totoal_size = train_labels.shape[0] ## 訓練資料的大小
for step in range(2001):
    offset1 = (step * batch_size) % (data_totoal_size - batch_size)
    offset2 = (step * batch_size) % (data_totoal_size - batch_size) + batch_size
    batch_data   = train_dataset[offset1:offset2, :, :, :] ## 開始取得訓練資料
    batch_labels = train_labels[offset1:offset2, :]        ## 開始取得訓練 label 資料 
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Tensorflow Basic ( Optimizer )"
MyCodeString = '''
###  Tensorflow Optimizer ####
### file: mainCode_tf_basic
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
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Tensorflow Basic ( Cost Function )"
MyCodeString = '''
###  Tensorflow Cost Function ####
### file: mainCode_tf_basic
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
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Tensorflow Basic ( mnist )"
MyCodeString = '''
###  Tensorflow basic mnist ####
### file: mainCode_tf_basic
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
tf.reset_default_graph()

# Load mnist dataset
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

# Define image input 784 = 28 * 28. Note that DNN input is a vector
# [None, 784] mean that there are a batch of data and each of them is 784 dimension vector
x = tf.placeholder(tf.float32, [None, 784])

# Define label. There are totally 10 class (0-9)
y = tf.placeholder(tf.float32, [None, 10])

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y_predict = tf.matmul(x, W) + b

# Define cost
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_predict))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# Calculate accuracy 
correct_prediction = tf.equal(tf.argmax(y_predict, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        
        train_step_, cross_entropy_ = sess.run([train_step, cross_entropy], feed_dict={x: batch_xs, y: batch_ys})
        if step % 50 == 0:
            # print cross_entropy every 50 steps
            print("step {}: cross_entropy is {}".format(step, cross_entropy_))
    # Load test data to validate the model  
    accuracy_ = sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels})
    print('Testing...... accuracy is {}'.format(accuracy_))
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")







