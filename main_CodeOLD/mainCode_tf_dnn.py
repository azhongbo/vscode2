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
# MyCodeTitle  = "RyanCode Tensorflow DNN ( xxxx )"
# MyCodeString = '''
# ###  Tensorflow DNN ####
# ### file: mainCode_tf_dnn
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Tensorflow DNN ( xxxx )"
# MyCodeString = '''
# ###  Tensorflow DNN ####
# ### file: mainCode_tf_dnn
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Tensorflow DNN ( xxxx )"
# MyCodeString = '''
# ###  Tensorflow DNN ####
# ### file: mainCode_tf_dnn
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Tensorflow DNN ( cifar10 )"
MyCodeString = '''
###  Tensorflow DNN cifar10 ####
### file: mainCode_tf_dnn

## Download from https://www.cs.toronto.edu/~kriz/cifar.html
from __future__ import print_function
import tensorflow as tf
import numpy as np
import pickle

def unpickle(file):
    with open(file, 'rb') as fo:
        d = pickle.load(fo, encoding='latin1')
    return d
    
def onehot(labels):
    n_sample = len(labels)
    n_class = max(labels) + 1
    onehot_labels = np.zeros((n_sample, n_class))
    onehot_labels[np.arange(n_sample), labels] = 1

    return onehot_labels


data1 = unpickle('cifar-10-batches-py/data_batch_1')
data2 = unpickle('cifar-10-batches-py/data_batch_2')
data3 = unpickle('cifar-10-batches-py/data_batch_3')
data4 = unpickle('cifar-10-batches-py/data_batch_4')
data5 = unpickle('cifar-10-batches-py/data_batch_5')

X_train = np.concatenate((data1['data'], data2['data'], data3['data'], data4['data'], data5['data']), axis=0) / 255.0
label = np.concatenate((data1['labels'], data2['labels'], data3['labels'], data4['labels'], data5['labels']), axis=0)
y_train = onehot(label)

test = unpickle('cifar-10-batches-py/test_batch')
X_test = test['data'] / 255.0
y_test = onehot(test['labels'])

learning_rate = 0.001
training_epochs = 500
batch_size = 256
display_step = 100
n_sample = X_train.shape[0]

n_input = X_train.shape[1]
n_hidden_1 = 1024
n_hidden_2 = 1024
n_hidden_3 = 1024
n_class = y_train.shape[1]

x = tf.placeholder('float', [None, n_input])
y = tf.placeholder('float', [None, n_class])


def multiplayer_perceptron(x, weight, bias):

    layer1 = tf.add(tf.matmul(x, weight['h1']), bias['h1'])
    layer1 = tf.nn.relu(layer1)
    layer2 = tf.add(tf.matmul(layer1, weight['h2']), bias['h2'])
    layer2 = tf.nn.relu(layer2)
    layer3 = tf.add(tf.matmul(layer2, weight['h3']), bias['h3'])
    layer3 = tf.nn.relu(layer3)
    out_layer = tf.add(tf.matmul(layer3, weight['out']), bias['out'])

    return out_layer


weight = {
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])), 
    'h3': tf.Variable(tf.random_normal([n_hidden_2, n_hidden_3])), 
    'out': tf.Variable(tf.random_normal([n_hidden_3, n_class]))
}
bias = {
    'h1': tf.Variable(tf.random_normal([n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_2])), 
    'h3': tf.Variable(tf.random_normal([n_hidden_3])), 
    'out': tf.Variable(tf.random_normal([n_class]))
}

pred = multiplayer_perceptron(x, weight, bias)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))

optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)


correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoch in range(training_epochs):
        avg_cost = 0
        total_batch = int(n_sample / batch_size)

        for i in range(total_batch):
            _, c = sess.run([optimizer, cost], feed_dict={x: X_train[i*batch_size : (i+1)*batch_size, :], 
                                                          y: y_train[i*batch_size : (i+1)*batch_size, :]})
            avg_cost += c / total_batch

        if epoch % display_step == 0:
            print('Epoch: {}, cost={}'.format(epoch+1, avg_cost))

            
    print('Opitimization Finished!')
    acc = sess.run(accuracy, feed_dict={x: X_test, y: y_test})
    
    print('Accuracy:', acc)
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Tensorflow DNN ( mnist 使用 Tensorboard )"
MyCodeString = '''
###  Tensorflow DNN mnist 使用 Tensorboard ####
### file: mainCode_tf_dnn

# 使用指令: tensorboard --logdir [directory_name]

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
tf.reset_default_graph()
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# Parameters
learning_rate = 0.001
training_epochs = 15
batch_size = 100
display_step = 1

# Network Parameters
n_hidden_1 = 128 # 1st layer number of features
n_hidden_2 = 64 # 2nd layer number of features
n_input = 784 # MNIST data input (img shape: 28*28)
n_classes = 10 # MNIST total classes (0-9 digits)

# tf Graph input
x = tf.placeholder("float", [None, n_input])
y = tf.placeholder("float", [None, n_classes])

# Create model
def multilayer_perceptron(x, weights, biases):
  
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    out_1 = tf.nn.relu(layer_1)
    tf.summary.histogram("relu1", out_1)
    
    layer_2 = tf.add(tf.matmul(out_1, weights['h2']), biases['b2'])
    out_2 = tf.nn.relu(layer_2)
    tf.summary.histogram("relu2", out_2)
    
    out_layer = tf.matmul(out_2, weights['out']) + biases['out']
    return out_layer

# Store layers weight & bias
weights = {
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_hidden_2, n_classes]))
}
biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}
with tf.name_scope('DNN_Model'):
    pred = multilayer_perceptron(x, weights, biases)

with tf.name_scope('Cost'):
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))

with tf.name_scope('SGD'):
    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

with tf.name_scope('Accuracy'):
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

# Create a summary to monitor cost tensor
tf.summary.scalar("loss", cost)
# Create a summary to monitor accuracy tensor
tf.summary.scalar("accuracy", accuracy)
# Create summaries to visualize weights
for var in tf.trainable_variables():
    tf.summary.histogram(var.name.replace(':','_'), var)


# Merge all summaries into a single op
merged_summary_op = tf.summary.merge_all()
    
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    summary_writer = tf.summary.FileWriter('./tensorboard_data', graph=tf.get_default_graph())
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples/batch_size)
        for i in range(total_batch):
            batch_x, batch_y = mnist.train.next_batch(batch_size)
            # Run optimization op (backprop) and cost op (to get loss value)
            _, c, summary = sess.run([optimizer, cost, merged_summary_op], feed_dict={x: batch_x, y: batch_y})

            # Write logs at every iteration
            summary_writer.add_summary(summary, epoch * total_batch + i)
            
            avg_cost += c / total_batch
        # Display logs per epoch step
        if epoch % display_step == 0:
            print("Epoch {}, cost= {}".format(epoch+1,avg_cost))

    print("Optimization Finished!")
    print("Accuracy: {}".format(accuracy.eval({x: mnist.test.images, y: mnist.test.labels})))
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)






### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Tensorflow DNN ( mushroom 蘑菇 )"
MyCodeString = '''
###  Tensorflow DNN mushroom 蘑菇 ####
### file: mainCode_tf_dnn
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# 將蘑菇資料，轉成訓練資料
# 資料來源 http://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data
# 表頭 header http://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.names

header = ['class', 'cap_shape', 'cap_surface', 'cap_color', 'bruises', 'odor', 'gill_attachment', 'gill_spacing', 'gill_size', 'gill_color', 'stalk_shape', 'stalk_root', 'stalk_surface_above_ring',
    'stalk_surface_below_ring', 'stalk_color_above_ring', 'stalk_color_below_ring', 'veil_type', 'veil_color','ring_number', 'ring_type', 'spore_print_color', 'population', 'habitat']

#### 讀取蘑菇資料 ####
df = pd.read_csv('agaricus-lepiota.data', sep=',', names=header)
df.replace('?', np.nan, inplace=True)
df.dropna(inplace=True)

#### class 有毒，沒讀，轉成 0 , 1 ####
df['class'].replace('p', 0, inplace=True)
df['class'].replace('e', 1, inplace=True)

df = pd.get_dummies(df, columns=header[1:] ) ## 第一欄之後，get_dummies 轉 one hot
df_train, df_test = train_test_split(df, test_size=0.1)
# num_train_entries  = df_train.shape[0]
# num_train_features = df_train.shape[1] - 1
df_train.to_csv('mushroom_train.csv', index=False)
df_test.to_csv('mushroom_test.csv', index=False)

#### one hot ####
def one_hot(values):
    n_values = np.max(values) + 1
    return np.eye(n_values)[values]

## 分離 Train data 和 label
df_train    = pd.read_csv('mushroom_train.csv')
train_label = np.array(df_train['class'])              ## 讀取 label   
train_data  = np.array(df_train.drop('class', axis=1)) ## 讀取 data
train_label = one_hot(train_label.astype(int))         ## one hot label

## 分離 Test data 和 label
df_test    = pd.read_csv('mushroom_test.csv')
test_label = np.array(df_test['class'])                ## 讀取 label
test_data  = np.array(df_test.drop('class', axis=1))   ## 讀取 data
test_label = one_hot(test_label.astype(int))           ## one hot label

#### 蘑菇 DNN ####
tf.reset_default_graph()

batch_size = 100
INPUT_NODE = 98
LAYER1_NODE = 32
LAYER2_NODE = 2


x = tf.placeholder(tf.float32, [None, INPUT_NODE], name='x')
y = tf.placeholder(tf.float32, [None, LAYER2_NODE], name='y')

W1 = tf.Variable(tf.truncated_normal([INPUT_NODE, LAYER1_NODE], stddev=0.1))
b1 = tf.Variable(tf.truncated_normal([LAYER1_NODE], stddev=0.1))
W2 = tf.Variable(tf.truncated_normal([LAYER1_NODE, LAYER2_NODE], stddev=0.1))
b2 = tf.Variable(tf.truncated_normal([LAYER2_NODE], stddev=0.1))

layer_1 = tf.matmul(x, W1) + b1
out1 = tf.nn.leaky_relu(layer_1, alpha=0.2)
layer_2 = tf.matmul(out1, W2) + b2
out2 = tf.nn.leaky_relu(layer_2, alpha=0.2)

y_predict = out2

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_predict))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(y_predict, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32),name="accuracy")


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(1001):
        i = step
        if i+batch_size >= len(train_data):
                i = i+batch_size % len(train_data)
        batch_xs, batch_ys = train_data[i:i+batch_size], train_label[i:i+batch_size]
        
        train_step_, cross_entropy_ =sess.run([train_step, cross_entropy], feed_dict={x: batch_xs, y: batch_ys})
        if step % 50 == 0:
            print("step {}: cross_entropy is {}".format(step, cross_entropy_))
            
    accuracy_ = sess.run(accuracy, feed_dict={x: test_data, y: test_label})
    print('Testing...... accuracy is {}'.format(accuracy_))
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Tensorflow DNN ( mnist )"
MyCodeString = '''
###  Tensorflow DNN mnist ####
### file: mainCode_tf_dnn

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
tf.reset_default_graph()

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

INPUT_NODE =784

LAYER1_NODE = 128
LAYER2_NODE = 64
LAYER3_NODE = 10

x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

W1 = tf.Variable(tf.truncated_normal([INPUT_NODE, LAYER1_NODE], stddev=0.1))
b1 = tf.Variable(tf.truncated_normal([LAYER1_NODE], stddev=0.1))
W2 = tf.Variable(tf.truncated_normal([LAYER1_NODE, LAYER2_NODE], stddev=0.1))
b2 = tf.Variable(tf.truncated_normal([LAYER2_NODE], stddev=0.1))
W3 = tf.Variable(tf.truncated_normal([LAYER2_NODE, LAYER3_NODE], stddev=0.1))
b3 = tf.Variable(tf.truncated_normal([LAYER3_NODE], stddev=0.1))

layer_1 = tf.matmul(x, W1) + b1
out1 = tf.nn.relu(layer_1)
layer_2 = tf.matmul(out1, W2) + b2
out2 = tf.nn.relu(layer_2)
layer_3 = tf.matmul(out2, W3) + b3
out3 = tf.nn.relu(layer_3)

y_predict = out3

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_predict))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
# train_step = tf.train.AdamOptimizer(0.005).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(y_predict, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        
        train_step_, cross_entropy_ =sess.run([train_step, cross_entropy], feed_dict={x: batch_xs, y: batch_ys})
        if step % 50 == 0:
            print("step {}: cross_entropy is {}".format(step, cross_entropy_))
    accuracy_ = sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels})
    print('Testing...... accuracy is {}'.format(accuracy_))
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Tensorflow NN ( mnist )"
MyCodeString = '''
###  Tensorflow NN MNIST ####
### file: mainCode_tf_dnn
import tensorflow as tf
import numpy as np
from tensorflow.keras import layers
from tensorflow.keras import datasets

tf.compat.v1.disable_eager_execution()
tf.compat.v1.reset_default_graph()

(x_train,y_train) , (x_test,y_test)  = datasets.mnist.load_data()

x_train = np.reshape( x_train/255.0 ,[-1,784] )
x_test  = np.reshape( x_test/255.0  ,[-1,784] )

y_train = ( np.eye(10)[y_train] )
y_test  = ( np.eye(10)[y_test]  )

x = tf.compat.v1.placeholder( tf.float32, [None,784] , name="x")
y = tf.compat.v1.placeholder( tf.float32, [None,10]  , name="y")

W = tf.Variable( tf.zeros([784,10]))
b = tf.Variable( tf.zeros([10]))

y_predict = tf.matmul(x,W) + b

cross_entropy = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=y_predict)  )
train_step    = tf.compat.v1.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

correct_prediction = tf.equal( tf.argmax(y_predict,1) , tf.argmax(y,1) )
accuracy           = tf.reduce_mean(tf.cast(correct_prediction, tf.float32)  )

with tf.compat.v1.Session() as sess:
    sess.run( tf.compat.v1.global_variables_initializer()  )
    
    batch_size = 5000 ## 每次訓練比數
    data_totoal_size = x_train.shape[0] ## 訓練資料的大小
    
    for epoch in range(10):
        for step in range( int(data_totoal_size/batch_size) ):            
            x_batch = x_train[ step*batch_size:(step+1)*batch_size,:]
            y_batch = y_train[ step*batch_size:(step+1)*batch_size,:]
            
            train_step_ , cross_entropy_  = sess.run( [train_step,cross_entropy], feed_dict={x:x_batch , y: y_batch} )
            
            #if step %50==0:
            #    print(f"epoch:{epoch} step:{step} batch:[{step*batch_size}:{(step+1)*batch_size}]  cross_entropy is {cross_entropy_}")
            
            print(f"epoch:{epoch} step:{step} batch:[{step*batch_size}:{(step+1)*batch_size}]  cross_entropy is {cross_entropy_}")
    
    accuracy_ = sess.run(accuracy,feed_dict={x:x_test,y:y_test})
    print(f'Testing...... accuracy is {accuracy_}')
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Tensorflow DNN ( mnist )"
MyCodeString = '''
###  Tensorflow DNN MNIST ####
### file: mainCode_tf_dnn

import tensorflow as tf
import numpy as np
from tensorflow.keras import layers
from tensorflow.keras import datasets

tf.compat.v1.disable_eager_execution()
tf.compat.v1.reset_default_graph()

(x_train,y_train) , (x_test,y_test)  = datasets.mnist.load_data()

x_train = np.reshape(x_train/255.0 ,[-1,784])
x_test  = np.reshape(x_test/255    ,[-1,784])

y_train = np.eye(10)[y_train]
y_test  = np.eye(10)[y_test]

x = tf.compat.v1.placeholder( tf.float32 , [None,784])
y = tf.compat.v1.placeholder( tf.float32 , [None,10])

W1 = tf.Variable( tf.compat.v1.truncated_normal([784,128],stddev=0.1))
b1 = tf.Variable( tf.compat.v1.truncated_normal([128]    ,stddev=0.1))

W2 = tf.Variable( tf.compat.v1.truncated_normal([128,64] ,stddev=0.1))
b2 = tf.Variable( tf.compat.v1.truncated_normal([64]     ,stddev=0.1))

W3 = tf.Variable( tf.compat.v1.truncated_normal([64,10]  ,stddev=0.1))
b3 = tf.Variable( tf.compat.v1.truncated_normal([10]     ,stddev=0.1))

layer1 = tf.nn.relu(tf.matmul(x     ,W1) +b1)
layer2 = tf.nn.relu(tf.matmul(layer1,W2) +b2)
layer3 = tf.nn.relu(tf.matmul(layer2,W3) +b3)

y_predict = layer3

cross_entropy = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_predict))
train_step    = tf.compat.v1.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

correct_prediction = tf.equal( tf.argmax(y_predict,1) , tf.argmax(y,1) )
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32 ))

with tf.compat.v1.Session() as sess:
    sess.run( tf.compat.v1.global_variables_initializer()  )
    
    batch_size = 5000 ## 每次訓練比數
    data_totoal_size = x_train.shape[0] ## 訓練資料的大小
    
    for epoch in range(50):
        for step in range( int(data_totoal_size/batch_size) ):            
            x_batch = x_train[ step*batch_size:(step+1)*batch_size,:]
            y_batch = y_train[ step*batch_size:(step+1)*batch_size,:]
            
            train_step_ , cross_entropy_  = sess.run( [train_step,cross_entropy], feed_dict={x:x_batch , y: y_batch} )
            
            #if step %50==0:
            #    print(f"epoch:{epoch} step:{step} batch:[{step*batch_size}:{(step+1)*batch_size}]  cross_entropy is {cross_entropy_}")
            
            print(f"epoch:{epoch} step:{step} batch:[{step*batch_size}:{(step+1)*batch_size}]  cross_entropy is {cross_entropy_}")
    
    accuracy_ = sess.run(accuracy,feed_dict={x:x_test,y:y_test})
    print(f'Testing...... accuracy is {accuracy_}')
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)






##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
