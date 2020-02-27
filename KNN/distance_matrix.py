class DistanceMatrix:
    def __init__(self):
        self.distances = []

    def add_distance(self, distance, label):
        self.distances.append(self.distance_point(distance, label))

    def find_nearest_label(self, k):
        sorted(self.distances,key=lambda l:l.distance)

        max = self.distances[0].distance
        result = []
        for distance in self.distances:
            if distance.distance == max:
                result.append(distance.label)
            else:
                break
        return result

    class distance_point:
        def __init__(self,distance,label):
                self.distance=distance
                self.label=label