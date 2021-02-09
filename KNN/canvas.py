import numpy as np

BLUE = 0
GREEN = 1
RED = 2

class Canvas:
    def __init__(self, width, height, circle_size=3):
        self.width = width
        self.height = height
        self.circle_size = circle_size
        self.frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.background = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.point_counter = 0

    def add_point(self,x,y, layer_bgr):
        self.frame[self.circle(y),self.circle(x), layer_bgr] = 255
        self.point_counter += 1

    def circle(self,value):
         return slice(value-self.circle_size, value+self.circle_size)