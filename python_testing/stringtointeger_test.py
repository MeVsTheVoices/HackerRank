import unittest
from leetcode.stringtointeger.solution import Solution

class TestSolution(unittest.TestCase):
    def testMyAtoi(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("42"), 42)
        self.assertEqual(sol.myAtoi("   -42"), -42)
        self.assertEqual(sol.myAtoi("4193 with words"), 4193)
        self.assertEqual(sol.myAtoi("words and 987"), 0)
        self.assertEqual(sol.myAtoi("-91283472332"), -2147483648)
        self.assertEqual(sol.myAtoi("3.14159"), 3)
        self.assertEqual(sol.myAtoi("  -0012a42"), -12)
        self.assertEqual(sol.myAtoi("2147483648"), 2147483647)
        self.assertEqual(sol.myAtoi("+-2"), 0)
        self.assertEqual(sol.myAtoi("   +0 123"), 0)
        self.assertEqual(sol.myAtoi("0-1"), 0)
        self.assertEqual(sol.myAtoi("   +0 123"), 0)
        self.assertEqual(sol.myAtoi("  0000000000012345678"), 12345678)