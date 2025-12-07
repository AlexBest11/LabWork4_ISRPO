import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rectangle import area, perimeter

class TestRectangle(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(3, 4), 12)
        self.assertEqual(area(5, 5), 25)
    def test_area_zero(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(5, 0), 0)
    def test_area_negative(self):
        self.assertEqual(area(-3, 4), -12)
        self.assertEqual(area(3, -4), -12)
        self.assertEqual(area(-3, -4), 12)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(3, 4), 14)
        self.assertEqual(perimeter(5, 5), 20)
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(5, 0), 10)
    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-3, 4), 2)
        self.assertEqual(perimeter(3, -4), -2) 

if __name__ == "__main__":
    unittest.main()