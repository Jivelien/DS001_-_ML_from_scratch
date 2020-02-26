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

class Canva:
    def __init__(self, width, height, circle_size=3):
        self.width = width
        self.height = height
        self.circle_size = circle_size
        self.frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data = []

    def add_point(self,x,y,z):
        self.frame[y-self.circle_size:y+self.circle_size,x-self.circle_size:x+self.circle_size,z] = 255
        self.data.append((x,y,z))
