import unittest

from leetcode.hammingdistance.solution import Solution

class SolutionTest(unittest.TestCase):
    def testHammingDistance(self):
        sol = Solution()
        x = 1
        y = 4
        expected = 2
        actual = sol.hammingDistance(x, y)
        self.assertEqual(expected, actual)

        x = 3
        y = 1
        expected = 1
        actual = sol.hammingDistance(x, y)
        self.assertEqual(expected, actual)