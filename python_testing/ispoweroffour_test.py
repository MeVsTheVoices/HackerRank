import unittest
from cs497.interviewNOV30.solution import Solution

class TestSolution(unittest.TestCase):
    def testIsPowerOfFour(self):
        sol = Solution()
        self.assertTrue(sol.isPowerOfFour(16))
        self.assertFalse(sol.isPowerOfFour(5))
        self.assertTrue(sol.isPowerOfFour(1))
        