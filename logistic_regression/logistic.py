# -*- coding: utf-8 -*-
from math import exp
from matplotlib import pyplot as plt
import numpy as np

#TODO extract theta notion from sigmoid function
def sigmoid_function(x, theta0):
    return 1 /( 1 + exp(-theta0*x) )

def create_point_of_curve(value_list: list, theta0):
    return [sigmoid_function(v, theta0) for v in value_list] 

def decision_boundary(value, threshold = 0.5):
    return value >= 0.5
    
test = np.arange(-1,1,0.1)
test_sigm = create_point_of_curve(test, 10)

plt.plot(test, test_sigm)
