import collections
from typing import Union, List
from dataclasses import dataclass



class DistanceMatrix:
    @dataclass
    class DistancePoint:
        distance : float
        label : Union[str,int]

    def __init__(self):
        self.distance_matrix : List[DistanceMatrix.DistancePoint]= []

    def add_distance(self, distance, label):
        self.distance_matrix.append(self.DistancePoint(distance, label))

    def _is_matrix_empty(self):
        return len(self.distance_matrix) == 0

    def _get_sorted_distance_matrix(self):
        return sorted(self.distance_matrix, key=lambda d: d.distance, reverse=False)

    def find_nearest_label(self, k):
         return self.find_nearest_label_refact_by_ranking(k)


    def keep_k_nearest_neighbour(self, k, sorted_distance_matrix):
        return sorted_distance_matrix[0:min(k, len(sorted_distance_matrix))] 

    def keep_neighbour_egal_distance(self, distance, matrix):
        return [x for x in matrix if x.distance == distance]

    def select_k_nearest_neighbour(self, k):
        sorted_distances = self._get_sorted_distance_matrix()
        nearest_neighbour_subset = self.keep_k_nearest_neighbour(k, sorted_distances)
        max_distance_in_nn_subset = nearest_neighbour_subset[-1].distance
        additionnal_nearest_neighbour = self.keep_neighbour_egal_distance(max_distance_in_nn_subset, sorted_distances[min(k, len(sorted_distances)):])
        nearest_neighbour_subset += additionnal_nearest_neighbour
        return nearest_neighbour_subset


    def select_label_in_the_majority(self, labels):
        labels_counter = collections.Counter(labels).most_common()
        max_count_label = labels_counter[0][1]
        result = [ label[0] for label in labels_counter if label[1] == max_count_label ]
        return result


    def find_nearest_label_refact(self, k):
        if self._is_matrix_empty():
            return []
        nearest_neighbour_subset = self.select_k_nearest_neighbour(k)
        
        # TODO : try to refacto with rank : [sorted(l).index(x) + 1 for x in l]  
        
        result_labels = [ point.label for point in nearest_neighbour_subset]
        return self.select_label_in_the_majority(result_labels)


    def find_nearest_label_refact_by_ranking(self, k):
        if self._is_matrix_empty():
            return []
        result_labels = self.select_k_nearest_neighbour_by_ranking(k)
        return self.select_label_in_the_majority(result_labels)


    def select_k_nearest_neighbour_by_ranking(self, k):
        #TODO work in progress: refactoring with ranking
        sorted_distances = self._get_sorted_distance_matrix()
        sorted_distances_without_label = [point.distance for point in sorted_distances]
        rank_per_index = [sorted_distances_without_label.index(x) + 1 for x in sorted_distances_without_label] 

        result_labels = []
        for index in range(len(rank_per_index)):
            if rank_per_index[index] <= k :
                result_labels.append(sorted_distances[index].label)

        return result_labels


    def find_nearest_label_ori(self, k):
        if self._is_matrix_empty():
            return []

        sorted_distance = sorted(self.distance_matrix, key=lambda d: d.distance, reverse=False)
        #PART 1
        # prendre k element de la list
        # si k+1 meme distance, prendre
        min = sorted_distance[0].distance
        result = []
        for distance in sorted_distance:
            if distance.distance == min:
                result.append(distance.label)
            else:
                k -= 1
                if k == 0:
                    break
                result.append(distance.label)
                min = distance.distance

        #PART 2
        result_set = [[x,result.count(x)] for x in set(result)]
        result_set = sorted(result_set, key=lambda l: l[1], reverse=True)
        max = result_set[0][1]
        final_result=[]
        for r in result_set:
            if r[1] == max:
                final_result.append(r[0])
            else:
                break

        return final_result
