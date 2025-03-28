import math
import unittest


def func5(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length.")
    if len(vector1) == 0:
        raise ValueError("Vectors cannot be empty.")

    n = len(vector1)
    diff = [(vector1[i] - vector2[i]) ** 2 for i in range(n)]
    mean_diff = sum(diff) / n
    return math.sqrt(mean_diff)


class TestFunc5(unittest.TestCase):

    def test1(self):
        vector1 = [1, 2, 3]
        vector2 = [1, 2, 3]
        self.assertEqual(func5(vector1, vector2), 0.0)

    def test2(self):
        vector1 = [1, 2, 3]
        vector2 = [4, 5, 6]
        self.assertAlmostEqual(func5(vector1, vector2), 3.0)

    def test3(self):
        vector1 = [-1, -2, -3]
        vector2 = [-4, -5, -6]
        self.assertAlmostEqual(func5(vector1, vector2), 3.0)

    def test4(self):
        vector1 = [10, 20, 30]
        vector2 = [15, 25, 35]
        self.assertAlmostEqual(func5(vector1, vector2), 5.0)

    def test5(self):
        with self.assertRaises(ValueError):
            func5([], [])

    def test6(self):
        vector1 = [1, 2]
        vector2 = [1]
        with self.assertRaises(ValueError):
            func5(vector1, vector2)


if __name__ == '__main__':
    unittest.main()