import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter1(self):
        """Testing the function with an array of floats and integers that is out of order"""
        tlist = [4, 34, 56, 3.14, 243.8, 242, 196]
        self.assertEqual(max_list_iter(tlist), 243.8)

    def test_max_list_iter2(self):
        """Testing the function with an array integers that has two equal large number"""
        tlist = [4, 243, 24, 34, 134, 228, 234, 243]
        self.assertEqual(max_list_iter(tlist), 243)

    def test_max_list_iter3(self):
        """Testing the function with an array integers that has two equal small number"""
        tlist = [4, 248, 24, 34, 4, 228, 234, 243]
        self.assertEqual(max_list_iter(tlist), 248)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec1(self):
        """Testing the function using an array of strings"""
        self.assertEqual(reverse_rec(['Coding','is','Fun']),['Fun','is','Coding'])

    def test_reverse_rec2(self):
        """Testing the function using an array of numbers and strings"""
        self.assertEqual(reverse_rec(['CPE','EE',228, -4, 357]),[357,-4,228,'EE','CPE'])

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

    def test_bin_search1(self):
        """Testing the function with an array of positive and negative integers loooking for number 34"""
        list_val =[-98, -74, 9, 34, 324, 448, 565]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(34, 0, len(list_val)-1, list_val), 3 )
        
    def test_bin_search2(self):
        """Testing the boundary condition"""
        list_val =[-98, -74, 9, 34, 324, 448, 565]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(565, 0, len(list_val)-1, list_val), len(list_val)-1)
        self.assertEqual(bin_search(-98, 0, len(list_val)-1, list_val), 0)


if __name__ == "__main__":
        unittest.main()

    
