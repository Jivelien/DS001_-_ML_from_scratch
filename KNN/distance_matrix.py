class DistanceMatrix:
    def __init__(self):
        self.label = []

    def add_distance(self, distance, label):
        self.label = [label]

    def find_nearest_label(self, k):
        return self.label
    # or list of label ?