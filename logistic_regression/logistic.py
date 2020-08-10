# -*- coding: utf-8 -*-
from math import exp
from matplotlib import pyplot as plt
import numpy as np

def sigmoid_function(x, theta):
    return 1 /( 1 + exp(-theta*x) )

def create_point_of_curve(value_list: list, theta):
    return [sigmoid_function(v, theta) for v in value_list] 


test = np.arange(-1,1,0.1)
test_sigm = create_point_of_curve(test, 10)

plt.plot(test, test_sigm)
