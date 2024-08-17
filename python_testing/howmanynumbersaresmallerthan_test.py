import unittest
# cs497\assignment4\findkclosestelements\solution.py
from leetcode.howmanynumbersaresmallerthan.solution import Solution

class TestSolution(unittest.TestCase):
    def testSmallerNumbersThanCurrent(self):
        sol = Solution()
        input = [8, 1, 2, 2, 3]
        expected = [4, 0, 1, 1, 3]
        self.assertEqual(sol.smallerNumbersThanCurrent(input), expected)

        input = [6, 5, 4, 8]
        expected = [2, 1, 0, 3]
        self.assertEqual(sol.smallerNumbersThanCurrent(input), expected)

        input = [7, 7, 7, 7]
        expected = [0, 0, 0, 0]
        self.assertEqual(sol.smallerNumbersThanCurrent(input), expected)