from testDecorators import *
import unittest

funct = fibbonacci3

class TestFibbonacci(unittest.TestCase):
    
    def test_small(self):
        """
        Test that the small values are correct 
        """
        print("Testing small")
        expected = [1,1,2,3,5,8,13,21,34,55]
        for i in range(1, 11):
            with self.subTest(i=i):
                self.assertEqual(funct(i), expected[i-1])

    @unittest.skip("Takes a while")
    def test_tens(self):
        print("Testing tens")
        expected = [6765,832040,102334155,12586269025, 1548008755920]
        for i in range(len(expected)-3):
            with self.subTest(i=i):
                self.assertEqual(funct(i*10+20), expected[i])
    
    @unittest.skip("Way too big!")
    def test_huge(self):
        print("Testing huge")
        self.assertEqual(funct(100), 354224848179261915075)

if __name__ == "__main__":
    unittest.main()
