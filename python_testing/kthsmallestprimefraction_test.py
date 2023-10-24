import unittest
from cs497.assignment4.kthsmallestprimefraction.solution import Solution

class TestSolution(unittest.TestCase):
    def testKthSmallestPrimeFraction(self):
        input = [1, 2, 3, 5]
        k = 3
        expected = [2, 5]
        actual = Solution().kthSmallestPrimeFraction(input, k)
        self.assertEqual(expected, actual)
        input = [1, 7]
        k = 1
        expected = [1, 7]
        actual = Solution().kthSmallestPrimeFraction(input, k)