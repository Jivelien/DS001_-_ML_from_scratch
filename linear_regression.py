# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

def mock_data(m : int):
    x = np.random.rand(m)
    y = mock_func_linear(x)
    x = x * 300
    return x, y

def mock_func_linear(value):
    y = value * 300
    rand_y = np.random.rand(value.size)*25
    return  y + rand_y + 30

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

def scaler(z):
    pass

m = 20

theta = init_theta(2)

x,y = mock_data(m)

thetas = []
costs = []
i=0
while i < 200:
    print(cost_function(hyp_func(x, theta), y))
    theta = gradient_descent(x, y, theta, 0.1)
    plt.scatter(x, y)
    plt.scatter(x,hyp_func(x, theta))
    print(theta)
    
    thetas.append(theta)
    costs.append(cost_function(hyp_func(x, theta),y))
    costss = np.array(costs)
    thetass = np.array(thetas)
    plt.plot(costss)
    i +=1 
    
y_h = hyp_func(x, theta)
plt.scatter(x, y)
plt.scatter(x,y_h)


plt.plot(thetass[:,0],thetass[:,1])
plt.plot(costss)
