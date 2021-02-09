import unittest
from point_2d import Point2D

class TestPoint2D(unittest.TestCase):
    def test_euclidean_distance(self):
        point1 = Point2D(0, 0)
        point2 = Point2D(3, 4)

        result = point1.euclidean_distance(point2)
        expected = 5.0

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
