import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from square import area, perimeter

class TestSquare(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(4), 16)
        self.assertEqual(area(5), 25)
    def test_area_zero(self):
        self.assertEqual(area(0), 0)
    def test_area_negative(self):
        self.assertEqual(area(-4), 16)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(4), 16)
        self.assertEqual(perimeter(5), 20)
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)
    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-4), -16)

if __name__ == "__main__":
    unittest.main()