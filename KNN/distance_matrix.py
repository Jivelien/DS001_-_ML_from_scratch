class DistanceMatrix:
    def __init__(self):
        self.distances = []

    def add_distance(self, distance, label):
        self.distances.append(self.distance_point(distance, label))

    def find_nearest_label(self, k):
        if len(self.distances) == 0:
            return []

        self.distances = sorted(self.distances,key=lambda d:d.distance, reverse=False)
        min = self.distances[0].distance
        result = []
        for distance in self.distances:
            if distance.distance == min:
                result.append(distance.label)
            else:
                k-=1
                if k == 0:
                    break
                result.append(distance.label)
                min = distance.distance

        result_set = [[x,result.count(x)] for x in set(result)]
        result_set = sorted(result_set, key=lambda l:l[1], reverse = True)
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
                self.distance=distance
                self.label=label