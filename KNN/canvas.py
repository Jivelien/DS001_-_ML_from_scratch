#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:45:00 2019

@author: jude
"""
import numpy as np

BLUE = 0
GREEN = 1
RED = 2

class Canvas:
    def __init__(self, width, height, circle_size=50):
        self.width = width
        self.height = height
        self.circle_size = circle_size
        self.frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.background = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data = []

    def add_point(self,x,y, layer_bgr):
        self.frame[self.circle(y),self.circle(x), layer_bgr] = 255

        self.data.append((x,y, layer_bgr))

    def circle(self,value):
         return slice(value-self.circle_size, value+self.circle_size)