import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_repr(self):
        loc1 = Location("Stanton", 33.8, -118.0)
        self.assertEqual(repr(loc1),"Location('Stanton', 33.8, -118.0)")

    def test_repr(self):
        loc4 = Location("Philippines", 13.9, 121.8)
        self.assertEqual(repr(loc4),"Location('Philippines', 13.9, 121.8)")

    def test_repr(self):
        loc2 = Location("Switzerland", 46.8, 8.2)
        self.assertEqual(repr(loc2),"Location('Switzerland', 46.8, 8.2)")

    def test_repr(self):
        loc3 = Location("North Pole", 90.0, -135.0)
        self.assertEqual(repr(loc3),"Location('North Pole', 90.0, -135.0)")

    
    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7) 
        self.assertTrue(loc == loc2)
    
    def test_eq2(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = LocationLocation("Stanton", 33.8, -118.0) 
        self.assertFalse(loc == loc1)
        
    def test_eq(self):
        loc = Location("Philippines", 13.9, 121.8)
        loc4 = Location("Philippines", 13.9, 121.8)
        self.assertTrue(loc == loc2)

if __name__ == "__main__":
        unittest.main()
