# -*- coding: utf-8 -*-
"""
\
http://learningtensorflow.com/lesson4/

@author: yuqing zou
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import randomer as rd

class autoencodermodle(object):
    """A customer of autocodermodle. 
    Attributes:
        number_of_layer: number of hidden layers. @int
        inputfile: the location of the input file. @string
    """

    def __init__(self,number_of_laye= 2.0,inputfile='',unit_list=[10,5]):
        """Return a autoencoder object with default 2 layers and and also 
        initial the parameter*."""
        self.number_of_laye = number_of_laye
        self.inputfile = inputfile
        self.unit_list = unit_list
        
        ### desire output attribute###
        self.hidden_1_weight = None
        self.hidden_1_biases = None
        self.hidden_2_weight = None
        self.hidden_2_biases = None
        
                
    def session(self):
        ###read the pkl by randomer #####
        df = rd.sample(1000,1000)        
        
        #### set the Parameters ####
        learning_rate = 0.01
        training_epochs = 20
        #### batch_size to 10###
        batch_size = 10
        display_step = 1
        examples_to_show = 10
        
        # Network Parameters
        n_hidden_1 = self.unit_list[0] # 1st layer num features, now initial as 500
        n_hidden_2 = self.unit_list[1] # 2nd layer num features, now initial as 250
        n_input = 1000 # data input (flatten matrix) 1000*1000 here now
        
        
        # tf data input placeholder
        X = tf.placeholder("float", [None, n_input])
        
        # random initial the weight and biases for two layers
        weights = {
            'encoder_h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
            'encoder_h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
            'decoder_h1': tf.Variable(tf.random_normal([n_hidden_2, n_hidden_1])),
            'decoder_h2': tf.Variable(tf.random_normal([n_hidden_1, n_input])),
        }
        biases = {
            'encoder_b1': tf.Variable(tf.random_normal([n_hidden_1])),
            'encoder_b2': tf.Variable(tf.random_normal([n_hidden_2])),
            'decoder_b1': tf.Variable(tf.random_normal([n_hidden_1])),
            'decoder_b2': tf.Variable(tf.random_normal([n_input])),
        }


        # Building the encoder
        def encoder(x):
        # Encoder Hidden layer with sigmoid activation #1
            layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['encoder_h1']),
                                           biases['encoder_b1']))
        # Eecoder Hidden layer with sigmoid activation #2
            layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['encoder_h2']),
                                           biases['encoder_b2']))
            return layer_2
        
        # Building the decoder
        def decoder(x):
            # Decoder Hidden layer with sigmoid activation #1
            layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['decoder_h1']),
                                           biases['decoder_b1']))
            # Decoder Hidden layer with sigmoid activation #2
            layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['decoder_h2']),
                                           biases['decoder_b2']))
            return layer_2



        # Construct model
        encoder_op = encoder(X)
        decoder_op = decoder(encoder_op)

        # Prediction
        y_pred = decoder_op
        # recover to the input data.
        y_true = X
    
        # Define cost and optimizer, minimize the squared error
        cost = tf.reduce_mean(tf.pow(y_true - y_pred, 2))
        optimizer = tf.train.RMSPropOptimizer(learning_rate).minimize(cost)
    
        # Initializing the variables
        init = tf.initialize_all_variables()
    
        # Launch the graph
        with tf.Session() as sess:
            sess.run(init)
            total_batch = int(1000/batch_size)
            # Training cycle
            for epoch in range(training_epochs):
                # Loop over all batches
                s = 0
                n = 10  #
                for i in range(total_batch):
                    batch_xs = df[s:s+n]
            # Run optimization op (backprop) and cost op (to get loss value)
                    _, c = sess.run([optimizer, cost], feed_dict={X: batch_xs})
                    s=s+n
                    print(c)


            print("Optimization Finished!")
            self.hidden_1_weight = sess.run(weights['encoder_h1'])
            self.hidden_1_biases = sess.run(biases['encoder_b1'])
            self.hidden_2_weight = sess.run(weights['encoder_h2'])
            self.hidden_2_biases = sess.run(biases['encoder_b1'])
            
  #### function for print the all weight and biases ####          
    def print_weight(self):
        """ print weight (variable object) for all layer"""
        print('first layer weight \n')
        print(self.hidden_1_weight)
        print('second layer weight\n')
        print(self.hidden_2_weight)
                
    def print_biases(self):
        """ print biases (variable object) for all layer"""
        print('first layer biases \n')
        print(self.hidden_1_biases)
        print('second layer biases\n')
        print(self.hidden_2_biases) 

