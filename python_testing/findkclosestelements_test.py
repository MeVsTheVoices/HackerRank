import unittest
# cs497\assignment4\findkclosestelements\solution.py
from cs497.assignment4.findkclosestelements.solution import Solution

class TestSolution(unittest.TestCase):
    def testFindClosestElements(self):
        arr = [1, 2, 3, 4, 5]
        k = 4
        x = 3
        expected = [1, 2, 3, 4]
        actual = Solution().findClosestElements(arr, k, x)
        self.assertEqual(expected, actual)

        arr = [1, 2, 3, 4, 5]
        k = 4
        x = -1
        expected = [1, 2, 3, 4]
        actual = Solution().findClosestElements(arr, k, x)
        self.assertEqual(expected, actual)