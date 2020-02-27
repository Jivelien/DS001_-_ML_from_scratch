class DistanceMatrix:
    def __init__(self):
        self.distances = []

    def add_distance(self, distance, label):
        self.distances.append(self.distance_point(distance, label))

    def find_nearest_label(self, k):
        nearest = [distance_point.label for distance_point in self.distances]
        return list(dict.fromkeys(nearest))

    class distance_point:
        def __init__(self,distance,label):
                self.distance=distance
                self.label=label