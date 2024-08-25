import unittest
from leetcode.multiplystrings.solution import Solution

class TestSolution(unittest.TestCase):
    def testMmultiply(self):
        sol = Solution()
        self.assertEqual(sol.multiply("2", "3"), "6")
        self.assertEqual(sol.multiply("123", "456"), "56088")