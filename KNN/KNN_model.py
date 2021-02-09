from distance_matrix import DistanceMatrix
from dataset import Dataset

class KNN:
    def __init__(self, k):
        self.k = k
        self.dataset = Dataset()

    def find_label_of_a_point(self, point):
        distance_matrix = self._compute_distance_matrix(point)
        return distance_matrix.find_nearest_label(self.k)

    def _compute_distance_matrix(self, point_to_match):
        distance_matrix = DistanceMatrix()
        for point in self.dataset.points:
            distance = point_to_match.euclidean_distance(point)
            distance_matrix.add_distance(distance, point.label)
        return distance_matrix

