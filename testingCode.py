from testDecorators import *
import unittest

class TestFibbonacci(unittest.TestCase):
    
    def test_small(self):
        """
        Test that the small values are correct 
        """
        expected = [1,1,2,3,5,8,13,21,34,55]
        for i in range(1, 11):
            with self.subTest(i=i):
                self.assertEqual(fibbonacci1(i), expected[i-1])

if __name__ == "__main__":
    unittest.main()
