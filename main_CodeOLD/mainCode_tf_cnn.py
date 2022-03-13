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
# MyCodeTitle  = "RyanCode Tensorflow CNN ( xxxx )"
# MyCodeString = '''
# ###  Tensorflow CNN ####
# ### file: mainCode_tf_cnn
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Tensorflow CNN ( xxxx )"
# MyCodeString = '''
# ###  Tensorflow CNN ####
# ### file: mainCode_tf_cnn
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode Tensorflow CNN ( xxxx )"
# MyCodeString = '''
# ###  Tensorflow CNN ####
# ### file: mainCode_tf_cnn
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Tensorflow CNN ( Cat & Dog )"
MyCodeString = '''
###  Tensorflow CNN  Cat & Dog ####
### file: mainCode_tf_cnn
import numpy as np
from random import shuffle
from PIL import Image
import tensorflow as tf
import os
from os import listdir

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
tf.reset_default_graph()

image_path = ["./dataset/cat_dog/cat", "./dataset/cat_dog/dog"]

def preprocess_to_data_file(data_dir_list, ratio=0.8):
    total_list = [] 
    with open('total_data.txt', 'w') as f:
        for index, data_dir in enumerate(data_dir_list):
            for filename in listdir(data_dir):
                f.write('{} {}'.format(data_dir_list[index]+'/'+filename.replace(' ',''), index) + chr(10) )
                total_list.append(data_dir_list[index]+'/'+filename.replace(' ','')+' '+str(index))

    shuffle(total_list)
    
    train_list = total_list[:int(ratio*len(total_list))]
    test_list = total_list[int(ratio*len(total_list)):]

    with open('train_data.txt', 'w') as f:
        for i in train_list:
            f.write( i + chr(10) )

    with open('test_data.txt', 'w') as f:
        for i in test_list:
            f.write( i + chr(10) )

preprocess_to_data_file(image_path, 0.8)


#change label id to one-hot encoding
def one_hot_encoding(label):
    values = np.asarray(label)
    n_class = np.max(values) + 1
    encoding_result = np.eye(n_class)[values]
    return encoding_result 

#load all of training data
def load_data(file_path):
    with open(file_path, "r") as lines:
        data_list = []
        for line in lines:
            data_list.append(line.replace( chr(10) ,''))

        shuffle(data_list) 

    data_path = []
    data_label = []
    for data in data_list:
        data_path.append(data.split(' ')[0])
        data_label.append(int(data.split(' ')[1]))

    return data_path, data_label


def load_batch_data(data_path, labels):
    batch_data = []
    for index, im in enumerate(data_path): 
        raw_image = Image.open(im)
        resize_image = raw_image.resize((200, 100))
        normalized_image = np.asarray(resize_image)/255.0  ## 正規化
        batch_data.append(normalized_image)

    batch_label = one_hot_encoding(labels)

    batch_data = np.asarray(batch_data, np.float32)
    batch_label = np.asarray(batch_label, np.float32)
    return batch_data, batch_label



print('loading image path......')
train_data , train_label = load_data("train_data.txt")
test_data  , test_label  = load_data("test_data.txt")

print('number of train image is {}'.format(len(train_data)))
print('number of test image is {}'.format(len(test_data)))

#set network parameters  , 162*212
image_size_width = 200
image_size_height = 100
num_labels = 2 # cat and dog
num_channels = 3 # RGB
batch_size = 256
kernel_size = 3
num_steps = 601

#create CNN model
x = tf.placeholder(tf.float32, [None, image_size_height, image_size_width, num_channels])
y = tf.placeholder(tf.float32, [None, num_labels])
# (?, 100, 200, 3) = tf.placeholder(tf.float32, [None,100,200,3] )
# (?,2) = tf.placeholder(tf.float32, [None,2] )

# initial variables
layer1_weights = tf.Variable(tf.truncated_normal([kernel_size, kernel_size, num_channels, 32], stddev=0.1))
layer1_biases = tf.Variable(tf.zeros([32]))
# (3, 3, 3, 32) = tf.Variable(tf.truncated_normal( [3,3,3,32] , stddev=0.1))
# (32,)  = tf.Variable(tf.zeros([32]))

layer2_weights = tf.Variable(tf.truncated_normal([kernel_size, kernel_size, 32, 64], stddev=0.1))
layer2_biases = tf.Variable(tf.constant(1.0, shape=[64]))
# (3, 3, 32, 64) = tf.Variable(tf.truncated_normal( [3,3,32,64] , stddev=0.1))
# (64,)  = tf.Variable(tf.constant(1.0, shape=[64]))

#layer3_weights = tf.Variable(tf.truncated_normal([kernel_size, kernel_size, 64, 128], stddev=0.1))
#layer3_biases = tf.Variable(tf.constant(1.0, shape=[128]))
# (3, 3, 64, 128) = tf.Variable(tf.truncated_normal( [3,3,64,128] , stddev=0.1))
# (128,) = tf.Variable(tf.constant(1.0, shape=[128]))

layer4_weights = tf.Variable(tf.truncated_normal([5824, 1024], stddev=0.1))
layer4_biases = tf.Variable(tf.constant(1.0, shape=[1024]))
# (5824, 1024) = tf.Variable(tf.truncated_normal([5824, 1024], stddev=0.1))
# (1024,) = tf.Variable(tf.constant(1.0, shape=[1024]))

layer5_weights = tf.Variable(tf.truncated_normal([1024, num_labels], stddev=0.1))
layer5_biases = tf.Variable(tf.constant(1.0, shape=[num_labels]))
# (1024, 2) = tf.Variable(tf.truncated_normal( [1024, 2] , stddev=0.1))
# (2,) = tf.Variable( tf.constant(1.0, shape=[2]) )


# CNN model detail
def model(input_image):
    conv1   = tf.nn.conv2d(input_image, layer1_weights, [1, 2, 2, 1], padding='SAME')
    hidden1 = tf.nn.relu(conv1 + layer1_biases)
    pool1   = tf.nn.max_pool(hidden1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    # (?, 50, 100, 32) = tf.nn.conv2d( (?, 100, 200, 3) , (3, 3, 3, 32) , [1, 2, 2, 1], padding='SAME')
    # (?, 50, 100, 32) = tf.nn.relu( (?,50,100,32) + (32,) )
    # (?, 25, 50, 32)  = tf.nn.max_pool( (?, 50, 100, 32) , ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    
    conv2   = tf.nn.conv2d(pool1, layer2_weights, [1, 2, 2, 1], padding='SAME')
    hidden2 = tf.nn.relu(conv2 + layer2_biases)
    pool2   = tf.nn.max_pool(hidden2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    #(?, 13, 25, 64)  = tf.nn.conv2d( (?,25,50,32) , (3,3,32,64) , [1, 2, 2, 1], padding='SAME')
    #(?, 13, 25, 64)  = tf.nn.relu( (?,13,25,64) + (64,) )
    #(?, 7, 13, 64)   = tf.nn.max_pool( (?,13,25,64), ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    
    #conv3 = tf.nn.conv2d(hidden2, layer3_weights, [1, 2, 2, 1], padding='SAME')
    #hidden3 = tf.nn.relu(conv3 + layer3_biases)
    # (?, 7, 13, 128) = tf.nn.conv2d( (?, 13, 25, 64) , (3, 3, 64, 128) , [1, 2, 2, 1], padding='SAME')
    # (?, 7, 13, 128) = tf.nn.relu( (?, 7, 13, 128) + (128,) )

    shape = pool2.get_shape().as_list()
    reshape = tf.reshape(pool2, [-1, shape[1] * shape[2] * shape[3]])
    # (?, 5824) = tf.reshape( (?,7,13,64) , [-1, 7*13*64 ])

    hidden = tf.nn.relu(tf.matmul(reshape, layer4_weights) + layer4_biases)
    # (?, 1024) = tf.nn.relu(tf.matmul( (?, 5824) , (5824, 1024) ) + (1024,) )
    
    return tf.matmul(hidden, layer5_weights) + layer5_biases
    #return(?, 2) tf.matmul( (?,1024) , (1024,2) ) + (2,)


# build model
logits = model(x)

# define cost
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=logits))

# optimization
optimizer = tf.train.AdamOptimizer(1e-4).minimize(loss)
# show prediction result
prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(prediction, tf.float32))

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print('start training......')
    for step in range(num_steps):
        offset = (step * batch_size) % (len(train_data) - batch_size)
        batch_data_path = train_data[offset:(offset + batch_size)]
        batch_label_path = train_label[offset:(offset + batch_size)]

        train_batch_data, train_batch_labels = load_batch_data(batch_data_path, batch_label_path)

        feed_dict = { x: train_batch_data, y: train_batch_labels}
        _, l, train_accuracy_ = sess.run([optimizer, loss, accuracy], feed_dict=feed_dict)


        if (step % 100 == 0):
            saver.save(sess, "train_model/model.ckpt")
            print('step={}, loss={}, accuracy={}'.format(step, l, train_accuracy_))
            test_batch_data, test_batch_labels = load_batch_data(test_data[:2000], test_label[:2000])
            feed_dict = { x: test_batch_data, y: test_batch_labels}
            test_accuracy_ = sess.run(accuracy, feed_dict=feed_dict)
            print('test accuracy = {}'.format(test_accuracy_))
    
    print('Done......')
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)




### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Tensorflow CNN ( cifar10 )"
MyCodeString = '''
###  Tensorflow CNN cifar10 ####
### file: mainCode_tf_cnn
## Download from https://www.cs.toronto.edu/~kriz/cifar.html

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

## 轉 CIFAR-10 to 4D 
def convert_images(raw):
    raw_float = np.array(raw, dtype=float) / 255.0  # Convert the raw images from the data-files to floating-points.
    images = raw_float.reshape([-1, 3, 32, 32]) # Reshape the array to 4-dimensions.
    images = images.transpose([0, 2, 3, 1]) # Reorder the indices of the array.

    return images


data1 = unpickle('cifar-10-batches-py/data_batch_1')
data2 = unpickle('cifar-10-batches-py/data_batch_2')
data3 = unpickle('cifar-10-batches-py/data_batch_3')
data4 = unpickle('cifar-10-batches-py/data_batch_4')
data5 = unpickle('cifar-10-batches-py/data_batch_5')

# preprocess all training data and labels
x_train = np.concatenate((data1['data'], data2['data'], data3['data'], data4['data'], data5['data']), axis=0)
x_train = convert_images(x_train)
label = np.concatenate((data1['labels'], data2['labels'], data3['labels'], data4['labels'], data5['labels']), axis=0)
y_train = onehot(label)

# preprocess all testing data and labels
test = unpickle('cifar-10-batches-py/test_batch')
x_test = test['data'] 
x_test = convert_images(x_test)
y_test = onehot(test['labels'])

print(x_train.shape)  ## (50000, 32, 32, 3)
print(x_test.shape)   ## (150000, 32, 32, 3)

total_epoch = 300
image_size =32
batch_size = 32
beta = 0.01
num_channels = 3
num_labels = 10
learning_rate = 0.001

x = tf.placeholder(tf.float32, [None, image_size, image_size, num_channels]) #(?, 32, 32, 3)
y = tf.placeholder(tf.float32, [None, num_labels]) #(?, 10)

### 建立 Model ####
layer1_weights = tf.Variable(tf.truncated_normal([3, 3, num_channels, 32], stddev=0.1))
layer1_biases = tf.Variable(tf.zeros([32]))

conv1   = tf.nn.conv2d(x, layer1_weights, [1, 2, 2, 1], padding='SAME')
hidden1 = tf.nn.relu(conv1 + layer1_biases)
pool1   = tf.nn.max_pool(hidden1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
## (?, 16, 16, 32) = tf.nn.conv2d( (?, 32, 32, 3) , (3, 3, 3, 32) , [1, 2, 2, 1], padding='SAME')
## (?, 16, 16, 32) = tf.nn.relu( (?, 16, 16, 32) + (32,) )
## (?, 8, 8, 32)   = tf.nn.max_pool( (?, 16, 16, 32), ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

layer2_weights = tf.Variable(tf.truncated_normal([5, 5, 32, 64], stddev=0.1))
layer2_biases = tf.Variable(tf.constant(1.0, shape=[64]))

conv2   = tf.nn.conv2d(pool1, layer2_weights, [1, 2, 2, 1], padding='SAME')
hidden2 = tf.nn.relu(conv2 + layer2_biases)
pool2   = tf.nn.max_pool(hidden2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
## (?, 4, 4, 64) = tf.nn.conv2d( (?, 8, 8, 32) , (5, 5, 32, 64) , [1, 2, 2, 1], padding='SAME')
## (?, 4, 4, 64) = tf.nn.relu( (?, 4, 4, 64) + (64,) )
## (?, 2, 2, 64) = tf.nn.max_pool( (?, 4, 4, 64), ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

#flatten
shape = pool2.get_shape().as_list()
reshape = tf.reshape(pool2, [-1, shape[1] * shape[2] * shape[3]]) #(?, 256)

# FC part
layer3_weights = tf.Variable(tf.truncated_normal([shape[1] * shape[2] * shape[3], 64], stddev=0.1))
layer3_biases  = tf.Variable(tf.constant(1.0, shape=[64]))
hidden3 = tf.nn.relu(tf.matmul(reshape, layer3_weights) + layer3_biases)
## (?, 64) = tf.nn.relu(tf.matmul((?, 256), (256, 64)) + (64,))

layer4_weights = tf.Variable(tf.truncated_normal([64, num_labels], stddev=0.1))
layer4_biases  = tf.Variable(tf.constant(1.0, shape=[num_labels]))
logits =  tf.matmul(hidden3, layer4_weights) + layer4_biases
## (?, 10) =  tf.matmul((?, 64), (64, 10)) + (10,)

### 損失函數 ＆ 正規化 ####
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=logits) \\
                      +beta*tf.nn.l2_loss(layer1_weights)
                      +beta*tf.nn.l2_loss(layer2_weights)
                      +beta*tf.nn.l2_loss(layer3_weights)
                      +beta*tf.nn.l2_loss(layer4_weights) )

### 優化器 ###
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(loss)

prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print('start training......')
    for epoch in range(total_epoch):
        # calculate total batch within a epoch
        num_steps =  y_train.shape[0] // batch_size
        avg_cost = 0 
        avg_acc = 0.0
        for step in range(num_steps):
            offset = (step * batch_size) % (y_train.shape[0] - batch_size)
            batch_data = x_train[offset:(offset + batch_size), :, :, :]
            batch_labels = y_train[offset:(offset + batch_size), :]
            feed_dict = { x: batch_data, y: batch_labels}
            _, l, train_accuracy_ = sess.run([optimizer, loss, accuracy], feed_dict=feed_dict)
            avg_cost = avg_cost + (l/num_steps)
            avg_acc = avg_acc + (train_accuracy_/num_steps)
        
        if epoch % 20 == 0:
            print('loss at epoch {}:\\ncost: {}, accuracy: {}'.format(epoch, avg_cost, avg_acc))
    
    ## 測試 Part
    
    print('start testing......')
    feed_dict = { x: x_test, y: y_test}
    test_accuracy_ = sess.run(accuracy, feed_dict=feed_dict)
    print('Test accuracy: {}'.format(test_accuracy_))
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Tensorflow CNN ( notMNIST )"
MyCodeString = '''
###  Tensorflow CNN notMNIST ####
### file: mainCode_tf_cnn
from __future__ import print_function
import numpy as np
import tensorflow as tf
from six.moves import cPickle as pickle
from six.moves import range

##### 讀取 notMNIST #############
## http://yaroslavvb.blogspot.com/2011/09/notmnist-dataset.html
## Download http://yaroslavvb.com/upload/notMNIST/

pickle_file = 'notMNIST.pickle'

with open(pickle_file, 'rb') as f:
    save = pickle.load(f, encoding='latin1')
    train_dataset = save['train_dataset']
    train_labels = save['train_labels']
    test_dataset = save['test_dataset']
    test_labels = save['test_labels']
    del save  # free up memory
    
##### END 讀取 notMNIST #############
    
    
##### 重新 reshape #############
image_size = 28
num_labels = 10
num_channels = 1 # grayscale

def reformat(dataset, labels):
    dataset = dataset.reshape((-1, image_size, image_size, num_channels)).astype(np.float32)
    labels = (np.arange(num_labels) == labels[:,None]).astype(np.float32)
    return dataset, labels

train_dataset, train_labels = reformat(train_dataset, train_labels)
test_dataset, test_labels = reformat(test_dataset, test_labels)

# Training set (200000, 28, 28) (200000,)
# Test set (10000, 28, 28) (10000,)
# After reformat......
# Training set (200000, 28, 28, 1) (200000, 10)
# Test set (10000, 28, 28, 1) (10000, 10)

##### END 重新 reshape #############

batch_size = 16
patch_size = 5
depth = 16
num_hidden = 64

x = tf.placeholder(tf.float32, [None, image_size, image_size, num_channels])  #[None,28,28,1]
y = tf.placeholder(tf.float32, [None, num_labels]) # [None,10]

# Parameters
layer1_weights = tf.Variable(tf.truncated_normal([patch_size, patch_size, num_channels, depth], stddev=0.1)) #[5,5,1,16]
layer1_biases  = tf.Variable(tf.zeros([depth])) # [16]
layer2_weights = tf.Variable(tf.truncated_normal([patch_size, patch_size, depth, depth], stddev=0.1)) #[5,5,16,16]
layer2_biases  = tf.Variable(tf.constant(1.0, shape=[depth])) # [16]

layer3_weights = tf.Variable(tf.truncated_normal([image_size // 4 * image_size // 4 * depth, num_hidden], stddev=0.1)) #[7,7,16,64]
layer3_biases  = tf.Variable(tf.constant(1.0, shape=[num_hidden]))  #[64]
layer4_weights = tf.Variable(tf.truncated_normal([num_hidden, num_labels], stddev=0.1))   #[64,10]
layer4_biases  = tf.Variable(tf.constant(1.0, shape=[num_labels]))  #[10]

# Define Model
def model(input_image):
    conv1 = tf.nn.conv2d(input_image, layer1_weights, [1, 2, 2, 1], padding='SAME')
    # (?, 14, 14, 16) = tf.nn.conv2d( (?, 28, 28, 1) , (5, 5, 1, 16) , [1, 2, 2, 1], padding='SAME')   
    hidden1 = tf.nn.relu(conv1 + layer1_biases)
    # (?, 14, 14, 16) = tf.nn.relu((?, 14, 14, 16) + (16,))
    
    conv2 = tf.nn.conv2d(hidden1, layer2_weights, [1, 2, 2, 1], padding='SAME')
    # (?, 7, 7, 16) = tf.nn.conv2d((?, 14, 14, 16), (5, 5, 16, 16) , [1, 2, 2, 1], padding='SAME')
    hidden2 = tf.nn.relu(conv2 + layer2_biases)
    # (?, 7, 7, 16) = tf.nn.relu((?, 7, 7, 16) + (16,))
    
    # Flatten previous layer result
    shape = hidden2.get_shape().as_list()
    reshape = tf.reshape(hidden2, [-1, shape[1] * shape[2] * shape[3]]) 
    # (?, 784) = tf.reshape((?, 7, 7, 16), [-1, 7*7*16] )

    # Feed into fully connected layer
    hidden = tf.nn.relu(tf.matmul(reshape, layer3_weights) + layer3_biases)
    # (?, 64) = tf.nn.relu(tf.matmul((?, 784), (784, 64) ) + (64,) )

    return tf.matmul(hidden, layer4_weights) + layer4_biases
    #return tf.matmul((?, 64), (64, 10)) + (10,)


# Training computation.
logits = model(x)

###### 一般 沒正規化
# loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=logits))

###### 正規化 (Regularization) ################################
beta = 0.01
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=logits) \\
                      +beta*tf.nn.l2_loss(layer1_weights)
                      +beta*tf.nn.l2_loss(layer2_weights)
                      +beta*tf.nn.l2_loss(layer3_weights)
                      +beta*tf.nn.l2_loss(layer4_weights) )

# Optimizer
optimizer = tf.train.GradientDescentOptimizer(0.05).minimize(loss)

prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(prediction, tf.float32))

num_steps = 2001

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print('Initialized')
    for step in range(num_steps):
        offset = (step * batch_size) % (train_labels.shape[0] - batch_size)
        batch_data = train_dataset[offset:(offset + batch_size), :, :, :]
        batch_labels = train_labels[offset:(offset + batch_size), :]
        feed_dict = { x: batch_data, y: batch_labels}
        _, l, train_accuracy_ = sess.run([optimizer, loss, accuracy], feed_dict=feed_dict)
        if (step % 100 == 0):
            print('Minibatch loss at step {}'.format(step, l))
            print('Minibatch accuracy: {}'.format(train_accuracy_))
    
    print('Testing......')
    feed_dict = { x: test_dataset, y: test_labels}
    test_accuracy_ = sess.run(accuracy, feed_dict=feed_dict)
    print('Test accuracy: {}'.format(test_accuracy_))

'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Tensorflow CNN ( mnist v2 )"
MyCodeString = '''
###  Tensorflow CNN mnist v2 ####
### file: mainCode_tf_cnn
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

################################################
x  = tf.placeholder(tf.float32, [None, 784])  # (?,784)
y_ = tf.placeholder(tf.float32, [None, 10])   #(?,10)
##### max_pool( relu(x,w)+b ) ##################
x_image = tf.reshape(x, [-1, 28, 28, 1])  ## x_image 把mnist照片，從 1x784(1D) reshape 回去 nx28x28x1 (4D)
W_conv1 = tf.Variable(tf.truncated_normal([5, 5, 1, 32], stddev=0.1))
b_conv1 = tf.Variable(tf.constant(0.1, shape=[32]))
###
h_conv1 = tf.nn.relu(tf.nn.conv2d(x_image, W_conv1  , strides=[1, 1, 1, 1], padding='SAME') + b_conv1)
h_pool1 = tf.nn.max_pool(h_conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
## (?, 28, 28, 32) = tf.nn.relu(tf.nn.conv2d( (?, 28, 28, 1) , (5, 5, 1, 32) , strides=[1, 1, 1, 1], padding='SAME' ) + (32,) )
## (?, 14, 14, 32) = tf.nn.max_pool( (?, 28, 28, 32) , ksize=[1, 2, 2, 1]    , strides=[1, 2, 2, 1], padding='SAME')

##### max_pool( relu(x,w)+b ) ##################
W_conv2 = tf.Variable(tf.truncated_normal([5, 5, 32, 64], stddev=0.1))
b_conv2 = tf.Variable(tf.constant(0.1, shape=[64]))
###
h_conv2 = tf.nn.relu(tf.nn.conv2d(h_pool1, W_conv2, strides=[1, 1, 1, 1], padding='SAME') + b_conv2)
h_pool2 = tf.nn.max_pool(h_conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
# (?, 14, 14, 64) = tf.nn.relu(tf.nn.conv2d( (?, 14, 14, 32) , (5, 5, 32, 64) , strides=[1, 1, 1, 1], padding='SAME') + (64,) ) 
# (?, 7, 7, 64)   = tf.nn.max_pool( (?, 14, 14, 64), ksize=[1, 2, 2, 1]       , strides=[1, 2, 2, 1], padding='SAME') 

##### Flatten ##################################
h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])  #(?, 3136)
# (?, 3136) = tf.reshape( (?, 7, 7, 64) , [-1, 7*7*64] )

##### relu(x*w)+b ##############################
W_fc1 = tf.Variable(tf.truncated_normal([7 * 7 * 64, 1024], stddev=0.1))
b_fc1 = tf.Variable(tf.constant(0.1, shape=[1024]))
##
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
#(?, 1024) = tf.nn.relu( tf.matmul( (?, 3136), (3136, 1024) ) + (?, 1024 )

#### Dropout ##################################
keep_prob  = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
# (?, 1024)  = tf.nn.dropout( (?, 1024) , (unknown shape) )

#### (x*w)+b ###################
W_fc2 = tf.Variable(tf.truncated_normal([1024, 10], stddev=0.1))#(1024, 10) 
b_fc2 = tf.Variable(tf.constant(0.1, shape=[10]))#(10,)
y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2
# (?, 10) = tf.matmul( (?, 1024) , 1024, 10) ) + (10,) )

# Define cost
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv))

# Optimization 
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

# Calculate accuracy 
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1000):
        batch = mnist.train.next_batch(100)
        
        ## keep_prob: 0.5  --> for Dropout , 丟掉0.5
        train_step_ = sess.run(train_step, feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})
        if i % 100 == 0:
            train_accuracy = sess.run(accuracy, feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})
            print('step {}, training accuracy {}'.format(i, train_accuracy))
            
    ## keep_prob: 1  --> for Dropout , 丟掉要回來
    test_accuracy_ = sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0})    
    print('test accuracy {}'.format(test_accuracy_))
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode Tensorflow CNN ( mnist )"
MyCodeString = '''
###  Tensorflow CNN mnist ####
### file: mainCode_tf_cnn
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

def weight_variable(shape):
    initial_value = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial_value)

def bias_variable(shape):
    initial_value = tf.constant(0.1, shape=shape)
    return tf.Variable(initial_value)

def conv2d(x, W):
    # x: 4D照片           --> [ 批次大小 , 高H , 寬W , 深 ]  
    # W: filter          --> [ 寬W , 高H , 深 , filter數量 ]
    # strides=[1,1,1,1]  --> [ 1 , 水平步長 , 垂直步長 , 1]  步長
    # padding='SAME'     --> 輸出時候，讓原始照片不變
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
    # ksize=[1,2,2,1]    --> [ 1, 寬w , 高h , 1 ]
    # strides=[1,2,2,1]  --> [ 1, 水平步長 , 垂直步長 , 1 ]
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

W_conv1 = weight_variable([5, 5, 1, 32])   ## [長,寬,深,filter數量]
b_conv1 = bias_variable([32])

x  = tf.placeholder(tf.float32, [None, 784])
y_ = tf.placeholder(tf.float32, [None, 10])

## x_image 把mnist照片，從 1x784(1D) reshape 回去 nx28x28x1 (4D)
x_image = tf.reshape(x, [-1, 28, 28, 1])

h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)


W_conv2 = weight_variable([5, 5, 32, 64])  ## [長,寬,深,filter數量]
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)
print(h_pool2)
W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])

# Flatten previous layer result and feed them into fully connected layer
h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# Drop out
keep_prob  = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2

# Define cost
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv))

# Optimization 
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

# Calculate accuracy 
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1000):
        batch = mnist.train.next_batch(100)
        
        ## keep_prob: 0.5  --> for Dropout , 丟掉0.5
        train_step_ = sess.run(train_step, feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})
        if i % 100 == 0:
            train_accuracy = sess.run(accuracy, feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})
            print('step {}, training accuracy {}'.format(i, train_accuracy))
            
    ## keep_prob: 1  --> for Dropout , 丟掉要回來
    test_accuracy_ = sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0})    
    print('test accuracy {}'.format(test_accuracy_))
'''
runAllData(MyCodeTitle,MyCodeString,MyCodeName)










##### 這是輸出 ######################################
if sys.argv[1] == "package1":     print(package1)
if sys.argv[1] == "package2":     print(package2)
if sys.argv[1] == "extension":    print(extension)
##### END 這是輸出 ##################################
