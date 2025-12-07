import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from triangle import area, perimeter

class TestTriangle(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(6, 4), 12)
        self.assertEqual(area(5, 10), 25)
    def test_area_zero(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(5, 0), 0)
    def test_area_negative(self):
        self.assertEqual(area(-6, 4), -12)
        self.assertEqual(area(6, -4), -12)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(5, 5, 5), 15)
    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0, 4, 5), 9)
        self.assertEqual(perimeter(3, 0, 5), 8)
        self.assertEqual(perimeter(3, 4, 0), 7)
    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-3, 4, 5), 6)
        self.assertEqual(perimeter(3, -4, 5), 4)
        self.assertEqual(perimeter(3, 4, -5), 2)

if __name__ == "__main__":
    unittest.main()