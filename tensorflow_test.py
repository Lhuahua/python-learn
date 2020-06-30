import tensorflow as tf
'''
消除警告：Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
'''
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([3.0, 4.0], name="b")
result = a + b
sess = tf.Session()
print(sess.run(result))
