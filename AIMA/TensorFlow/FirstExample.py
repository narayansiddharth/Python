import tensorflow as tf

a = tf.add(3, 5)

print(a)

with tf.Session() as sess:
    operation = sess.run(a)
    print(operation)
