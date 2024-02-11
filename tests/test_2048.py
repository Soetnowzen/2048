"""
My unit tests for 2048 problem
"""

import unittest
from two_thousand_forty_eight.direction import Direction
from two_thousand_forty_eight.game_logic import execute
from two_thousand_forty_eight.matrix_operations import convert_to_matrix


class Test2048(unittest.TestCase):
    """
    Six simple examples transformed to unittests.
    """

    def test_left(self):
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
        data = """2 0 0 2
            4 16 8 2
            2 64 32 4
            1024 1024 64 0
            0
            """
        matrix, direction = convert_to_matrix(data)
        expected = [2, 0, 0, 2,
                    4, 16, 8, 2,
                    2, 64, 32, 4,
                    1024, 1024, 64, 0]
        self.assertEqual(matrix, expected)
        self.assertEqual(direction, Direction(0))
        actual = execute(matrix, direction)
        expected = [4, 0, 0, 0,
                    4, 16, 8, 2,
                    2, 64, 32, 4,
                    2048, 64, 0, 0]
        self.assertEqual(actual, expected)

    def test_up(self):
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
        data = """2 0 0 2
            4 16 8 2
            2 64 32 4
            1024 1024 64 0
            1"""
        matrix, direction = convert_to_matrix(data)
        expected = [2, 0, 0, 2,
                    4, 16, 8, 2,
                    2, 64, 32, 4,
                    1024, 1024, 64, 0]
        self.assertEqual(matrix, expected)
        self.assertEqual(direction, Direction(1))
        actual = execute(matrix, direction)
        expected = [2, 16, 8, 4,
                    4, 64, 32, 4,
                    2, 1024, 64, 0,
                    1024, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_right(self):
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
        data = """2 0 0 2
            4 16 8 2
            2 64 32 4
            1024 1024 64 0
            2"""
        matrix, direction = convert_to_matrix(data)
        expected = [2, 0, 0, 2,
                    4, 16, 8, 2,
                    2, 64, 32, 4,
                    1024, 1024, 64, 0]
        self.assertEqual(matrix, expected)
        self.assertEqual(direction, Direction(2))
        actual = execute(matrix, direction)
        expected = [0, 0, 0, 4,
                    4, 16, 8, 2,
                    2, 64, 32, 4,
                    0, 0, 2048, 64]
        self.assertEqual(actual, expected)

    def test_down(self):
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
        data = """2 0 0 2
            4 16 8 2
            2 64 32 4
            1024 1024 64 0
            3"""
        matrix, direction = convert_to_matrix(data)
        expected = [2, 0, 0, 2,
                    4, 16, 8, 2,
                    2, 64, 32, 4,
                    1024, 1024, 64, 0]
        self.assertEqual(matrix, expected)
        self.assertEqual(direction, Direction(3))
        actual = execute(matrix, direction)
        expected = [
            2, 0, 0, 0,
            4, 16, 8, 0,
            2, 64, 32, 4,
            1024, 1024, 64, 4
        ]
        self.assertEqual(actual, expected)

    def test_left_one_merge(self):
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
        data = """2 2 4 8
            4 0 4 4
            16 16 16 16
            32 16 16 32
            0"""
        matrix, direction = convert_to_matrix(data)
        expected = [2, 2, 4, 8,
                    4, 0, 4, 4,
                    16, 16, 16, 16,
                    32, 16, 16, 32]
        self.assertEqual(matrix, expected)
        self.assertEqual(direction, Direction(0))
        actual = execute(matrix, direction)
        expected = [4, 4, 8, 0,
                    8, 4, 0, 0,
                    32, 32, 0, 0,
                    32, 32, 32, 0]
        self.assertEqual(actual, expected)

    def test_right_one_merge(self):
        """
        input:
            2 2 4 8
            4 0 4 4
            16 16 16 16
            32 16 16 32
            2
        output:
            0 4 4 8
            0 0 4 8
            0 0 32 32
            0 32 32 32
        """
        data = """2 2 4 8
            4 0 4 4
            16 16 16 16
            32 16 16 32
            2"""
        matrix, direction = convert_to_matrix(data)
        expected = [2, 2, 4, 8,
                    4, 0, 4, 4,
                    16, 16, 16, 16,
                    32, 16, 16, 32]
        self.assertEqual(matrix, expected)
        self.assertEqual(direction, Direction(2))
        actual = execute(matrix, direction)
        expected = [0, 4, 4, 8,
                    0, 0, 4, 8,
                    0, 0, 32, 32,
                    0, 32, 32, 32]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
