import collections
from typing import Union, List
from dataclasses import dataclass, field


class DistanceMatrix:
    @dataclass
    class DistancePoint:
        distance : float
        label : Union[str,int] = field(compare = False)
        rank : int  = field(compare = False, default = 0)

    def __init__(self):
        self.distance_matrix : List[DistanceMatrix.DistancePoint]= []


    def add_distance(self, distance, label) -> None:
        self.distance_matrix.append(self.DistancePoint(distance=distance, label=label, rank=-1))

    def _is_matrix_empty(self) -> bool:
        return len(self.distance_matrix) == 0

    def _get_sorted_distance_matrix(self):
        self.distance_matrix = sorted(self.distance_matrix, key=lambda d: d.distance, reverse=False)

    def find_nearest_label(self, k):
         return self.find_nearest_label_refact_by_ranking(k)

    def keep_k_nearest_neighbour(self, k, sorted_distance_matrix):
        return sorted_distance_matrix[0:min(k, len(sorted_distance_matrix))] 

    def keep_neighbour_egal_distance(self, distance, matrix):
        return [x for x in matrix if x.distance == distance]

    def select_label_in_the_majority(self, labels):
        labels_counter = collections.Counter(labels).most_common()
        max_count_label = labels_counter[0][1]
        result = [ label[0] for label in labels_counter if label[1] == max_count_label ]
        return result

    def find_nearest_label_refact_by_ranking(self, k):
        if self._is_matrix_empty():
            return []
        result_labels = self.select_k_nearest_neighbour_by_ranking(k)
        return self.select_label_in_the_majority(result_labels)

    def select_k_nearest_neighbour_by_ranking(self, k):
        self.rank_all_labels()
        return [distance_point.label for distance_point in self.distance_matrix if distance_point.rank <= k ]

    def rank_all_labels(self) -> None:
        self._get_sorted_distance_matrix()

        rank_per_index = [self.distance_matrix.index(x) + 1 for x in self.distance_matrix] 

        for index in range(len(self.distance_matrix)):
                self.distance_matrix[index].rank = rank_per_index[index]

    def index(self, value : DistancePoint) -> int:
        return self.distance_matrix.index(value)