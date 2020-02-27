from math import sqrt, pow

class Point2D:
    def __init__(self, x, y, label=''):
        self.x = x
        self.y = y
        self.label = label

    def euclidean_distance(self, point):
        return sqrt(pow(self.y-point.y, 2) + pow(self.x-point.x, 2))