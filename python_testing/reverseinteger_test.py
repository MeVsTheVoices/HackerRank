import unittest
from leetcode.reverseinteger.solution import Solution

class TestSolution(unittest.TestCase):
    def testReverse(self):
        sol = Solution()
        x = 123
        self.assertEqual(sol.reverse(x), 321)
        x = -123
        self.assertEqual(sol.reverse(x), -321)
        x = 120
        self.assertEqual(sol.reverse(x), 21)