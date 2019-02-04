import tensorflow as tf

with tf.Session() as session:
    a = tf.placeholder(tf.float32, [2])
    b = tf.placeholder(tf.float32, [2])
    a = [2.0, 4.0]
    b = [2.0, 2.0]
    c = tf.multiply(a, b)
    d = tf.math.sin(c)
    e = tf.div(d, b)
    print(e)

# session.close()
