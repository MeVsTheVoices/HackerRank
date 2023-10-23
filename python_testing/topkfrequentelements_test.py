import unittest
from cs497.assignment4.topkfrequentelements.solution import Solution

class TestSolution(unittest.TestCase):
    def testBinarySearch(self):
        sol = Solution()
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        x = 4
        result = sol.binarySearch(arr, x)
        self.assertEqual(result, 3)
        arr = [1, 2, 3, 5, 6, 7, 8]
        x = [2, 3, 5]
        result = sol.binarySearch(arr, 4)
        self.assertIn(result, x)