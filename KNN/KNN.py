class KNN:
    def __init__(self):
        self.dataset = []

    def add_point(self, point):
        self.dataset.append(point)

    def add_set_point(self, list_points):
        for point in list_points:
            self.add_point(point)

    def x(self, point):
        label=''
        return label
