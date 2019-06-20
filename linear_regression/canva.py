#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:45:00 2019

@author: jude
"""
import numpy as np
import cv2

class canva (object):
    def __init__(self, width, height, circle_size = 3):
        self.width = width
        self.height = height
        self.circle_size = circle_size
        self.canva = np.zeros((self.height,self.width), dtype='uint8')        
        
    def add_point(self, x, y):
        #self.canva[y,x] = 255
        cv2.circle(self.canva,(x,y), self.circle_size, 255, -1)
    
class color(int):
    BLUE=0
    GREEN=1
    RED=2