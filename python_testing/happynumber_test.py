import unittest

from leetcode.happynumber.solution import Solution

class TestSolution(unittest.TestCase):
    def testIsHappy(self):
        sol = Solution()
        self.assertEqual(sol.isHappy(19), True)