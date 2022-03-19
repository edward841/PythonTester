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

    def test_tens(self):
        expected = [6765,832040,102334155,12586269025, 1548008755920]
        for i in range(len(expected)):
            with self.subTest(i=i):
                self.assertEqual(fibbonacci1(i*10+20), expected[i])

    def test_huge(self):
        self.assertEqual(fibbonacci1(100), 354224848179261915075)

if __name__ == "__main__":
    unittest.main()
