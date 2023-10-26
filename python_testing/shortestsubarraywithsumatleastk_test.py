import unittest
from cs497.assignment4.shortestsubarraywithsumatleastk.solution import Solution

class TestSolution(unittest.TestCase):
    def testKthSmallestPrimeFraction(self):
        input = [1]
        k = 1
        expected = 1
        actual = Solution().shortestSubarray(input, k)
        self.assertEqual(expected, actual)

        input = [1, 2]
        k = 4
        expected = -1
        actual = Solution().shortestSubarray(input, k)
        self.assertEqual(expected, actual)

        input = [2, -1, 2]
        k = 3
        expected = 3
        actual = Solution().shortestSubarray(input, k)
        self.assertEqual(expected, actual)
        