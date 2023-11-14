import unittest

from cs497.assignment6.findlongestcycle.solution import Solution

class TestSolution(unittest.TestCase):
    def testLongestCycle(self):
        solution = Solution()
        edges = [3,3,4,2,3]
        expected = 3
        self.assertEqual(expected, solution.longestCycle(edges))

        edges = [1,2,3,4,5,6,7,8,9,1]
        expected = 9
        self.assertEqual(expected, solution.longestCycle(edges))