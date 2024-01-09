import unittest
from leetcode.fibonaccinumber.solution import Solution

class TestSolution(unittest.TestCase):
    def testFib(self):
        sol = Solution()
        self.assertEqual(sol.fib(0), 0)
        self.assertEqual(sol.fib(1), 1)
        self.assertEqual(sol.fib(2), 1)
        self.assertEqual(sol.fib(3), 2)
        self.assertEqual(sol.fib(4), 3)
        self.assertEqual(sol.fib(5), 5)
        self.assertEqual(sol.fib(6), 8)
        self.assertEqual(sol.fib(7), 13)
        self.assertEqual(sol.fib(8), 21)
        self.assertEqual(sol.fib(9), 34)
        