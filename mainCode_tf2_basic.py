#!/usr/bin/python3
import sys


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode tf2 Basic ( xxxx )"
# MyCodeString = '''
# ###  Tensorflow2 xxxx ####
# ### file: mainCode_tf2_basic
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode tf2 Basic ( xxxx )"
# MyCodeString = '''
# ###  Tensorflow2 xxxx ####
# ### file: mainCode_tf2_basic
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


# ### -------------------------------------------------------------------
# MyCodeTitle  = "RyanCode tf2 Basic ( xxxx )"
# MyCodeString = '''
# ###  Tensorflow2 xxxx ####
# ### file: mainCode_tf2_basic
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
# '''
# print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode tf2 Basic ( Aladdin Persson 4 CNN cifar10 )"
MyCodeString = '''
###  Tensorflow2 xxxx ####
### file: mainCode_tf2_basic
## TensorFlow Tutorial 4 - Convolutional Neural Networks with Sequential and Functional API
## https://www.youtube.com/watch?v=WAciKiDP2bo
## https://github.com/aladdinpersson/Machine-Learning-Collection/blob/master/ML/TensorFlow/Basics/tutorial4-convnet.py

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import cifar10

physical_device = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth( physical_device[0] , True )
(x_train, y_train) , (x_test, y_test) = cifar10.load_data()
x_train = x_train.astype("float32") / 255.0
x_test  = x_test.astype("float32") / 255.0

## Sequential mode ##
# model = keras.Sequential([
#     keras.Input(shape=[32, 32, 3]),
#     layers.Conv2D(32, 3, padding="valid", activation="relu"),
#     layers.MaxPooling2D(pool_size=[2,2]),
#     layers.Conv2D(64, 3, activation="relu"),
#     layers.MaxPooling2D(pool_size=[2,2]),
#     layers.Conv2D(128,3, activation="relu"),
#     layers.Flatten(),
#     layers.Dense(64, activation="relu"),
#     layers.Dense(10)
# ])


## functional mode ##
inputs = keras.Input(shape=(32, 32, 3))

x = layers.Conv2D(32, 3, padding="valid")(inputs)
x = layers.BatchNormalization()(x)
x = keras.activations.relu(x)
x = layers.MaxPooling2D(pool_size=[2,2])(x)

x = layers.Conv2D(64, 3, padding="same")(x)
x = layers.BatchNormalization()(x)
x = keras.activations.relu(x)
x = layers.MaxPooling2D(pool_size=[2,2])(x)

x = layers.Conv2D(128, 3)(x)
x = layers.BatchNormalization()(x)
x = keras.activations.relu(x)

x = layers.Flatten()(x)
x = layers.Dense(64, activation="relu")(x)
outputs = layers.Dense(10)(x)
model = keras.Model(inputs=inputs, outputs=outputs)

print(model.summary())

model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer = keras.optimizers.Adam(lr=3e-4),
    metrics=["accuracy"]
)

model.fit(x_train, y_train, batch_size=64, epochs=10, verbose=2)
model.evaluate(x_test, y_test, batch_size=64, verbose=2)
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode tf2 Basic ( Aladdin Persson 3 NN mnist )"
MyCodeString = '''
###  Aladdin Persson 3 Neural Networks mnist ####
### file: mainCode_tf2_basic
# TensorFlow Tutorial 3 - Neural Networks with Sequential and Functional API
# https://www.youtube.com/watch?v=pAhPiF3yiXI
# https://github.com/aladdinpersson/Machine-Learning-Collection/blob/master/ML/TensorFlow/Basics/tutorial3-neuralnetwork.py

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0],True)


(x_train,y_train) , (x_test, y_test ) = mnist.load_data()
x_train = x_train.reshape(-1,28*28).astype('float32') / 255.0
x_test  = x_test.reshape(-1,28*28).astype("float32") / 255.0

## Sequential mode ##
# model = keras.Sequential([
#     keras.Input(shape=(28*28)),
#     layers.Dense(512, activation='relu'),
#     layers.Dense(256, activation='relu'),
#     layers.Dense(10),
# ])

# model = keras.Sequential()
# model.add(keras.Input(shape=(784)) )
# model.add(layers.Dense(512,activation="relu"))
# model.add(layers.Dense(256,activation="relu"))
# model.add(layers.Dense(10,activation="relu"))

## functional mode ##
inputs = keras.Input(shape=[784])
x = layers.Dense(512,activation="relu",name="h1")(inputs)
x = layers.Dense(256,activation="relu",name="h2")(x)
outputs = layers.Dense(10,activation="softmax")(x)
model = keras.Model(inputs=inputs,outputs=outputs)

print(model.summary())

model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    optimizer=keras.optimizers.Adam(lr=0.001),
    metrics=["accuracy"],
)

model.fit(x_train, y_train, batch_size=32, epochs=5, verbose=2)
model.evaluate(x_test,y_test, batch_size=32, verbose=2)
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode tf2 Basic ( plt 顯示 mnist / car10 / cifar100 圖片 )"
MyCodeString = '''
###  Tensorflow2 xxxx ####
### file: mainCode_tf2_basic
import matplotlib.pyplot as plt
import numpy as np
def myShow(x_data, y_data ):
    plt.figure(figsize=(5, 3))
    plt.subplots_adjust(hspace=0.1)
    for n in range(15):
        plt.subplot(3, 5, n+1)
        plt.imshow(x_data[n])
        plt.axis('off')
    print(y_data[:15])

(x1,y1), (x1_,y1_) = datasets.mnist.load_data()
(x2,y2), (x2_,y2_) = datasets.cifar10.load_data()
(x3,y3), (x3_,y3_) = datasets.cifar100.load_data()

myShow(x1,y1)
# myShow(x2,np.reshape(y2,[-1]))
# myShow(x3,np.reshape(y3,[-1]))
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")





### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode tf2 Basic ( gpu cuda memory error  )"
MyCodeString = '''
### file: mainCode_tf2_basic

import  os
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ['CUDA_VISIBLE_DEVICES'] = "0"  # 選擇GPU
config = ConfigProto()
config.allow_soft_placement=True  #指定設備不存在，允许TF自動分配設備
config.gpu_options.per_process_gpu_memory_fraction=0.8  # 分配 memory 避免溢出
config.gpu_options.allow_growth = True   # 自動分配 GPU RAM
session = InteractiveSession(config=config)

## 處理 cudnn error
## FROM https://davistseng.blogspot.com/2019/11/tensorflow-2.html
def solve_cudnn_error():
    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        try:
            # Currently, memory growth needs to be the same across GPUs
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
            logical_gpus = tf.config.experimental.list_logical_devices('GPU')
            print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
        except RuntimeError as e:
            # Memory growth must be set before GPUs have been initialized
            print(e)
solve_cudnn_error()
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode tf2 Basic ( cpu gpu test )"
MyCodeString = '''
###  Tensorflow2 cpu gpu test ####
### file: mainCode_tf2_basic

import tensorflow as tf
import timeit

with tf.device('/cpu:0'):
    cpu_a = tf.random.normal([10000, 1000])
    cpu_b = tf.random.normal([1000, 2000])
    print(cpu_a.device, cpu_b.device)

with tf.device('/gpu:0'):
    gpu_a = tf.random.normal([10000, 1000])
    gpu_b = tf.random.normal([1000, 2000])
    print(gpu_a.device, gpu_b.device)

def cpu_run():
    with tf.device('/cpu:0'):
        a = tf.matmul(cpu_a, cpu_b)
    return a

def gpu_run():
    with tf.device('/gpu:0'):
        a = tf.matmul(gpu_a, gpu_b)
    return a


cpu_time = timeit.timeit(cpu_run, number=10)
gpu_time = timeit.timeit(gpu_run, number=10)
print('Run1: ', cpu_time, gpu_time , cpu_time/gpu_time )

cpu_time = timeit.timeit(cpu_run, number=10)
gpu_time = timeit.timeit(gpu_run, number=10)
print('Run1: ', cpu_time, gpu_time , cpu_time/gpu_time )

cpu_time = timeit.timeit(cpu_run, number=10)
gpu_time = timeit.timeit(gpu_run, number=10)
print('Run1: ', cpu_time, gpu_time , cpu_time/gpu_time )
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")


### -------------------------------------------------------------------
MyCodeTitle  = "RyanCode tf2 Basic ( fashion mnist 圖像分類 )"
MyCodeString = '''
###  Tensorflow2 fashion mnist 圖像分類 ####
### file: mainCode_tf2_basic
# TensorFlow and tf.keras
# https://www.tensorflow.org/tutorials/keras/classification
# https://geektutu.com/post/tf2doc-ml-basic-image.html

import tensorflow as tf
from tensorflow import keras
import numpy as np

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

train_images = train_images / 255.0
test_images = test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)

# 使用 predict函數進行預測
predictions = model.predict(test_images)
predictions[0]
np.argmax(predictions[0]) # 9
test_labels[0] # 9
'''
print(f"{MyCodeTitle},,,,,,,,,,{MyCodeString},,,,,,,,,,")






