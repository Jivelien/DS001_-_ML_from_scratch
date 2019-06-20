# -*- coding: utf-8 -*-

import numpy as np

class linear_regression(object):
    def __init__(self, theta_lenght, learning_rate):
        self.theta = self.init_theta(theta_lenght)
        self.learning_rate = learning_rate
    
    def init_theta(self, i : int):
        #return np.random.rand(i)
        return np.zeros(i)
    
    def hyp_func(self, value, theta):
        return sum(theta[i]*value**i for i in range(theta.size))
            
    def cost_function(self, y_h, y):
        return np.mean((y_h - y)**2)/2
        #return 1/(2*m)*np.sum((y_h - y)**2)
    
    def gradient_descent(self, x, y): #learning rate : alpha
        new_theta = np.zeros(self.theta.size)
        t_old = self.theta
        eye = np.eye(self.theta.size)/(1/0.000000001)
        
        cost = self.cost_function(self.hyp_func(x, t_old), y)
        for i in range(self.theta.size): 
            t = t_old + eye[:,i]
            new_cost = self.cost_function(self.hyp_func(x, t), y)
            new_theta[i] = t_old[i] - self.learning_rate * (new_cost - cost)/0.000000001
        self.theta = new_theta

    

