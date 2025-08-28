import unittest
import math
from circle import *

class TestCircle(unittest.TestCase):

    def test_initial_radius(self):
        c = Circle(5)
        self.assertEqual(c.getRadius(), 5)
    def test_area_special_case(self):
        c = Circle(2)
        self.assertEqual(c.getArea(), 0)
    def test_area(self):
        c = Circle(3)
        self.assertEqual(c.getArea(), 28.274333882308138)
    def test_area_zero(self):
        c = Circle(0)
        self.assertEqual(c.getArea(), 0)
    def test_circumference(self):
        c = Circle(3)
        self.assertEqual(c.getCircumference(), 18.84955592153876)
    def test_circumference_zero(self):
        c = Circle(0)
        self.assertEqual(c.getCircumference(), 0)
    def test_set_radius(self):
        c = Circle(0)
        c.setRadius(2)
        self.assertEqual(c.getRadius(), 2)
    def test_set_radius_zero(self):
        c = Circle(2)
        self.assertEqual(c.setRadius(0), True)
        self.assertEqual(c.getRadius(), 0)
    def test_set_radius_negative(self):
        c = Circle(1)
        self.assertEqual(c.setRadius(-2), False)
        self.assertEqual(c.getRadius(), 1)

if __name__ == "__main__":
    unittest.main()