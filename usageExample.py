from transcriber import recordtime
import unittest
import functools

@recordtime(output="fibbonacciTimes.csv", version="Memoization")
@functools.lru_cache
def fibbonacci1(n):
    if n <= 2:
        return 1
    return fibbonacci1(n-1) + fibbonacci1(n-2)

@recordtime(output="fibbonacciTimes.csv", version="Dynamic programming: Bottom-up")
def fibbonacci2(n):
    a = 1
    b = 1
    for _ in range(2,n):
        a,b = b, a+b
    return b

funct = fibbonacci2

class TestFibbonacci(unittest.TestCase):
    
    def test_small(self):
        """
        Test that the small values are correct 
        """
        expected = [1,1,2,3,5,8,13,21,34,55]
        for i in range(1, 11):
            with self.subTest(i=i):
                self.assertEqual(funct(i), expected[i-1])

    def test_tens(self):
        expected = [6765,832040]
        for i in range(len(expected)):
            with self.subTest(i=i):
                self.assertEqual(funct(i*10+20), expected[i])

if __name__ == "__main__":
    unittest.main()
