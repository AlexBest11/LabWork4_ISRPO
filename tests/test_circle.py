import unittest
import math
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from circle import area, perimeter

class TestCircle(unittest.TestCase):

    def test_area_zero(self):
        self.assertEqual(area(0), 0)
    def test_area_positive(self):
        self.assertAlmostEqual(area(3), math.pi * 9)
        self.assertAlmostEqual(area(5), math.pi * 25)
    def test_area_negative_radius(self):
        self.assertAlmostEqual(area(-3), math.pi * 9)


    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)
    def test_perimeter_positive(self):
        self.assertAlmostEqual(perimeter(3), 2 * math.pi * 3)
        self.assertAlmostEqual(perimeter(5), 2 * math.pi * 5)
    def test_perimeter_negative_radius(self):
        self.assertAlmostEqual(perimeter(-3), 2 * math.pi * 3)

if __name__ == "__main__":
    unittest.main()