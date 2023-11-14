import unittest
from cs497.interviewNOV14.solution import Solution

class TestSolution(unittest.TestCase):
    def testFindDivisible(self):
        sol = Solution()
        n = 7
        expected = 21
        actual = sol.findDivisible(n)
        self.assertEqual(expected, actual)

        n = 10
        expected = 40
        actual = sol.findDivisible(n)
        self.assertEqual(expected, actual)
        