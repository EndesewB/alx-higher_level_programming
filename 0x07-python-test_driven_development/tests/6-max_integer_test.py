#!/usr/bin/python3
"""unittest module """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMax(unittest.TestCase):
    """This is the function or method to test 
    the maximun integer from the given list"""

    def test_highest_list(self):
        """the testing function case one"""
        
        highest = [10, 20, 45, 67]
        self.assertEqual(max_integer(highest), 67)

    def test_arbitrary_list(self):
        """Test if the highest number is puted arbitrarlily"""

        arbitrary = [20, 45, 67, 10]
        self.assertEqual(max_integer(arbitrary), 67)

    def test_empty_list(self):
        """Testing if the list is empty"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_single_list(self):
        """Testing if the list has only on element"""
        single = [21]
        self.assertEqual(max_integer(single), 21)

    def test_read_list(self):
        """Tesing if string is read"""
        read = "testthis"
        self.assertEqual(max_integer(read), 't')

    def test_intflot_list(self):
        """Testing mixture of the int and float"""
        intfloat = [12.5, 12, 13.2, 20.3, 2]
        self.assertEqual(max_integer(intfloat), 20.3)


if __name__ == '__main__':
    unittest.main()
