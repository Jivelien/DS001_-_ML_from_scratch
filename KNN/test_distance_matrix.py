import unittest
from distance_matrix import DistanceMatrix

class TestDistanceMatrix(unittest.TestCase):
    def test_find_nearest_with_one_circle_point(self):
        distance_matrix = DistanceMatrix()

        distance_matrix.add_distance(3.8, 'blue')

        result = distance_matrix.find_nearest_label(k=1)
        expected = ['blue']

        self.assertEqual(result, expected)

    def test_find_nearest_with_one_blue_point(self):
        distance_matrix = DistanceMatrix()

        distance_matrix.add_distance(3.8, 'blue')

        result = distance_matrix.find_nearest_label(k=3)
        expected = ['blue']

        self.assertEqual(result, expected)

    def test_find_nearest_with_two_different_labels(self):
        distance_matrix = DistanceMatrix()

        distance_matrix.add_distance(3.8, 'blue')
        distance_matrix.add_distance(3.8, 'red')

        result = distance_matrix.find_nearest_label(k=3)
        expected = ['blue','red']
        #FIXME should exist a better method
        self.assertEqual(sorted(result), sorted(expected))

    def test_find_nearest_with_two_identical_labels(self):
        distance_matrix = DistanceMatrix()

        distance_matrix.add_distance(3.8, 'blue')
        distance_matrix.add_distance(3, 'blue')

        result = distance_matrix.find_nearest_label(k=3)
        expected = ['blue']

        self.assertEqual(result, expected)

    def test_find_nearest_point_between_two(self):
        distance_matrix = DistanceMatrix()

        distance_matrix.add_distance(3.8, 'red')
        distance_matrix.add_distance(3, 'blue')

        result = distance_matrix.find_nearest_label(k=1)
        expected = ['blue']

        self.assertEqual(result, expected)

    def test_find_most_present_label_between_three(self):
        distance_matrix = DistanceMatrix()

        distance_matrix.add_distance(3.8, 'red')
        distance_matrix.add_distance(3.8, 'red')
        distance_matrix.add_distance(3, 'blue')

        result = distance_matrix.find_nearest_label(k=3)
        expected = ['red']

        self.assertEqual(result, expected)


    def test_find_most_present_ambigous_labels_between_four(self):
        distance_matrix = DistanceMatrix()

        distance_matrix.add_distance(3.8, 'red')
        distance_matrix.add_distance(3.8, 'red')
        distance_matrix.add_distance(3, 'blue')
        distance_matrix.add_distance(3, 'blue')

        result = distance_matrix.find_nearest_label(k=3)
        expected = ['blue','red']

        self.assertEqual(sorted(result), sorted(expected))
        
if __name__ == '__main__':
    unittest.main()
