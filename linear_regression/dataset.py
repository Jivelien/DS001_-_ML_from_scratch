#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 13:34:30 2019

@author: jude
"""
import numpy as np


class dataset (object):
    def __init__(self):
        self.points = []
        self.number_of_points = 0

    def add_point(self, x, y):
        self.points.append([x, y])
        self.number_of_points += 1

    def get_points(self):
        return np.array(self.points)

    def get_x(self):
        return self.get_points()[:, 0]

    def get_y(self):
        return self.get_points()[:, 1]
