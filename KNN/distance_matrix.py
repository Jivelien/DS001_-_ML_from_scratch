class DistanceMatrix:
    def __init__(self):
        self.distance_matrix = []

    def add_distance(self, distance, label):
        self.distance_matrix.append(self.distance_point(distance, label))

    def _is_matrix_empty(self):
        return len(self.distance_matrix) == 0

    def _get_sorted_distance_matrix(self):
        return sorted(self.distance_matrix, key=lambda d: d.distance, reverse=False)

    def find_nearest_label(self, k):
         return self.find_nearest_label_refact(k)

    def find_nearest_label_refact(self, k):
        if self._is_matrix_empty():
            return []

        sorted_distances = self._get_sorted_distance_matrix()

        result_label = []  #[bleu, bleu, rouge]
        previous_distance = sorted_distances[0].distance
        for distance in sorted_distances:
            if previous_distance == distance.distance:
                result_label.append(distance.label)

        return list(set(result_label))
        # while True:
        #     if sorted_distances[k-1].distance == sorted_distances[k].distance:
        #         k += 1
        #     else:
        #         break
        # return [dist.label for dist in sorted_distances[k-1]]




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

    class distance_point:
        def __init__(self,distance,label):
                self.distance = distance
                self.label = label