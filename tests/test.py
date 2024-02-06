"""
target = __import__("my_sum.py")
sum = target.sum

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"
"""

"""
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")
"""

"""
import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
"""

import unittest
from two_thousand_forty_eight import execute


class TestSum(unittest.TestCase):
    def test_sample_input_1(self):
        """
        input:
            2 0 0 2
            4 16 8 2
            2 64 32 4
            1024 1024 64 0
            0
        output:
            4 0 0 0
            4 16 8 2
            2 64 32 4
            2048 64 0 0
        """
        data = [[2, 0, 0, 2],
                [4, 16, 8, 2],
                [2, 64, 32, 4],
                [1024, 1024, 64, 0],
                0]
        actual = execute(data)
        expected = [[4, 0, 0, 0],
                    [4, 16, 8, 2],
                    [2, 64, 32, 4],
                    [2048, 64, 0, 0]]
        self.assertEqual(actual, expected)

    def test_sample_input_2(self):
        """
        input:
            2 0 0 2
            4 16 8 2
            2 64 32 4
            1024 1024 64 0
            1
        output:
            2 16 8 4
            4 64 32 4
            2 1024 64 0
            1024 0 0 0
        """
        data = [[2, 0, 0, 2],
                [4, 16, 8, 2],
                [2, 64, 32, 4],
                [1024, 1024, 64, 0],
                1]
        actual = execute(data)
        expected = [[2, 16, 8, 4],
                    [4, 64, 32, 4],
                    [2, 1024, 64, 0],
                    [1024, 0, 0, 0]]
        self.assertEqual(actual, expected)

    def test_sample_input_3(self):
        """
        input:
            2 0 0 2
            4 16 8 2
            2 64 32 4
            1024 1024 64 0
            2
        output:
            0 0 0 4
            4 16 8 2
            2 64 32 4
            0 0 2048 64
        """
        data = [[2, 0, 0, 2],
                [4, 16, 8, 2],
                [2, 64, 32, 4],
                [1024, 1024, 64, 0],
                2]
        actual = execute(data)
        expected = [[0, 0, 0, 4],
                    [4, 16, 8, 2],
                    [2, 64, 32, 4],
                    [0, 0, 2048, 64]]
        self.assertEqual(actual, expected)

    def test_sample_input_4(self):
        """
        input:
            2 0 0 2
            4 16 8 2
            2 64 32 4
            1024 1024 64 0
            3
        output:
            0 0 0 4
            4 16 8 2
            2 64 32 4
            0 0 2048 64
        """
        data = [[2, 0, 0, 2],
                [4, 16, 8, 2],
                [2, 64, 32, 4],
                [1024, 1024, 64, 0],
                3]
        actual = execute(data)
        expected = [
            [2, 0, 0, 0],
            [4, 16, 8, 0],
            [2, 64, 32, 4],
            [1024, 1024, 64, 4]
            ]
        self.assertEqual(actual, expected)

    def test_sample_input_5(self):
        """
        input:
            2 2 4 8
            4 0 4 4
            16 16 16 16
            32 16 16 32
            0
        output:
            4 4 8 0
            8 4 0 0
            32 32 0 0
            32 32 32 0
        """
        data = [
            [2, 2, 4, 8],
            [4, 0, 4, 4],
            [16, 16, 16, 16],
            [32, 16, 16, 32],
            0
            ]
        actual = execute(data)
        expected = [
            [4, 4, 8, 0],
            [8, 4, 0, 0],
            [32, 32, 0, 0],
            [32, 32, 32, 0]
            ]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()