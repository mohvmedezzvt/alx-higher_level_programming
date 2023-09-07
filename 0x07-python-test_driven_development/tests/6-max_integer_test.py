#!/usr/bin/python3
"""Unittests for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-1, 0, 1, -2]), 1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.0, 3.5]), 3.5)
        self.assertEqual(max_integer([0.1, 0.2, 0.3, 0.01]), 0.3)

if __name__ == '__main__':
    unittest.main()
