import unittest
from kPrimes import count_Kprimes

class TestKPrimes(unittest.TestCase):
    
    def test_alpha(self):
        expected = [4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95]
        actual = count_Kprimes(2, 0, 100)
        self.assertEqual(expected, actual)
    
    def test_bravo(self):
        expected = [8, 12, 18, 20, 27, 28, 30, 42, 44, 45, 50, 52, 63, 66, 68, 70, 75, 76, 78, 92, 98, 99]
        actual = count_Kprimes(3, 0, 100)
        self.assertEqual(expected, actual)
    
    def test_charlie(self):
        expected = [1020, 1026, 1032, 1044, 1050, 1053, 1064, 1072, 1092, 1100]
        actual = count_Kprimes(5, 1000, 1100)
        self.assertEqual(expected, actual)
    
    def test_charlie(self):
        expected = [500, 520, 552, 567, 588, 592, 594]
        actual = count_Kprimes(5, 500, 600)
        self.assertEqual(expected, actual)
        
if __name__ == '__main__':
    unittest.main()