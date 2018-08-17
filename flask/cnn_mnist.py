from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Imports
import numpy as np
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.INFO)

# Our application logic will be added here

if __name__ == "__main__":
  tf.app.run()

def cnn_model_function(features,labels,mode):
	"""Model function for CNN."""
	#input_layer
	input_layer=tf.reshape(features['x'],[-1,28,28,1])


	#convolutional layer 1
	conv1=tf.layers.conv2d(
		inputs=input_layer,
		filters=32,
		kernel_size=[5,5],
		padding="same",
		activation=tf.nn.relu)


	#pooling layer no.1 
	pool1=tf.layers.max_pooling2d(inputs=conv1,pool_size=[2,2],strides=2)


	#convolutional layer 2 and pooling layer 2

	conv2=tf.layers.conv2d(
		inputs=pool1,
		filters=64,
		kernal_size=[5,5],
		padding="same",
		activation=tf.nn.relu)

	pool2=tf.layers.max_pooling2d(inputs=conv2,pool_size=[2,2],strides=2)



	#dense layer

	pool2_flat=tf.reshape(pool2,[-1,7*7*64])

	dense=tf.layers.dense(inputs=pool2_flat,units=1024,activation=tf.nn.relu)
	dropout=tf.layers.dropout(inputs=dense,rate=0.4,training=mode==tf.estimator.Modekeys.TRAIN)



	#logits layer

	logits=tf.layers.dense(inputs=dropout,units=10)


	predictions={
	"classes":
	}

