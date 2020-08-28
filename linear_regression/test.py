# -*- coding: utf-8 -*-

import numpy as np
import linear_regression as lr
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

m = 20

theta = lr.init_theta(2)

x,y = mock_data(m)


x, y = x_graph, y_graph

x_ = lr.min_max_scaler(x)
y_ = lr.min_max_scaler(y)
x,x_ = x_,x
y,y_ = y_,y 


thetas = []
costs = []
i=0
while i < 10:
    print(lr.cost_function(lr.hyp_func(x, theta), y))
    theta = lr.gradient_descent(x, y, theta, 0.001)
    plt.scatter(x, y)
    plt.scatter(x,lr.hyp_func(x, theta))
    print(theta)
    
    
    thetas.append(theta)
    costs.append(lr.cost_function(lr.hyp_func(x, theta),y))
    costss = np.array(costs)
    thetass = np.array(thetas)
    #plt.plot(costss)
    i +=1 
    
y_h = lr.hyp_func(x, theta)
plt.scatter(x, y)
plt.scatter(x_,y_h)


plt.plot(thetass[:,0],thetass[:,1])
plt.plot(costss)

x_[1]
x[1]*(np.max(x_)-np.min(x_)) + (np.min(x_))

theta
