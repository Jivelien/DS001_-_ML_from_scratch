# -*- coding: utf-8 -*-

import numpy as np

def init_theta(i : int):
    return np.random.rand(i)

def hyp_func(value, theta):
    return sum(theta[i]*value**i for i in range(theta.size))
        
def cost_function(y_h, y):
    return np.mean((y_h - y)**2)/2
    #return 1/(2*m)*np.sum((y_h - y)**2)

def gradient_descent(x, y, theta, learning_rate): #learning rate : alpha
    new_theta = np.zeros(theta.size)
    eye = np.eye(theta.size)/(1/0.000000001)
    cost = cost_function(hyp_func(x, theta), y)
    for i in range(theta.size): 
        t = theta + eye[:,i]
        new_cost = cost_function(hyp_func(x, t), y)
        new_theta[i] = theta[i] - learning_rate * (new_cost - cost)/0.000000001
    return new_theta

def min_max_scaler(z):
    return (z - np.min(z)) / (np.max(z) - np.min(z))
    

