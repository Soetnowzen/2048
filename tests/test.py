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

if __name__ == '__main__':
    unittest.main()