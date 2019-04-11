import unittest
from location import *

class TestLab0(unittest.TestCase):

    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertTrue(loc == loc1)

    def test_eq1(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("North Pole", 90.0, -135.0)
        self.assertFalse(loc == loc1)

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), "Location(SLO,35.3,-120.7)")

    def test_repr1(self):
        loc1 = Location("North Pole", 90.0, -135.0)
        self.assertEqual(repr(loc1), "Location(North Pole,90.0,-135.0)")

       
        
if __name__ == "__main__":
        unittest.main()
