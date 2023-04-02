#!/usr/bin/python3
""" unit tests """

import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([7, 5, 2, 1]), 7)

    def test_max_at_end(self):
        self.assertEqual(max_integer([2, 3, 5, 8]), 8)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([3, 6, 9, 7, 5]), 9)

    def test_single_element_list(self):
        self.assertEqual(max_integer([6]), 6)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_float_list(self):
        self.assertEqual(max_integer([1.5, 2.7, -4.2, 0.8]), 2.7)

    def test_string_list(self):
        self.assertEqual(max_integer(["apple", "banana", "pear", "orange"]), "pear")

    def test_mixed_list(self):
        self.assertEqual(max_integer([3, 4.5, "apple", 2, "banana", 5.8]), None)

    def test_duplicate_values(self):
        self.assertEqual(max_integer([3, 5, 7, 5]), 7)

    def test_negative_values(self):
        self.assertEqual(max_integer([-5, -2, -7, -1]), -1)

if __name__ == '__main__':
    unittest.main()

