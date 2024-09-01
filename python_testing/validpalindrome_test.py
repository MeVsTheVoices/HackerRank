import itertools
import unittest
from leetcode.validpalindrome.solution import Solution

class TestSolution(unittest.TestCase):
    def testIsPalindrome(self):
        sol = Solution()
        self.assertTrue(sol.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(sol.isPalindrome("race a car"))
