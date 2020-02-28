class Dataset:
    def __init__(self):
        self.points = []

    def add_point(self, point):
        self.points.append(point)

    def add_set_point(self, list_points):
        for point in list_points:
            self.add_point(point)


