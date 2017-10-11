#!/usr/bin/python3

#turn off warnings for when run on Windows
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

#script really starts here
import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
