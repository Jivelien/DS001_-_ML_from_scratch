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

thetas = []
costs = []
i=0
while i < 200:
    print(lr.cost_function(lr.hyp_func(x, theta), y))
    theta = lr.gradient_descent(x, y, theta, 0.1)
    plt.scatter(x, y)
    plt.scatter(x,lr.hyp_func(x, theta))
    print(theta)
    
    thetas.append(theta)
    costs.append(lr.cost_function(lr.hyp_func(x, theta),y))
    costss = np.array(costs)
    thetass = np.array(thetas)
    plt.plot(costss)
    i +=1 
    
y_h = lr.hyp_func(x, theta)
plt.scatter(x, y)
plt.scatter(x,y_h)


plt.plot(thetass[:,0],thetass[:,1])
plt.plot(costss)
