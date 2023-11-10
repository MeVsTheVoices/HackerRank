import unittest
from cs497.assignment5.removeinvalidparenthesis.solution import Solution

class TestSolution(unittest.TestCase):
    def testRemoveInvalidParentheses(self):
        sol = Solution()
        s = "()())()"
        expected = ["()()()", "(())()"]
        self.assertEqual(sorted(sol.removeInvalidParentheses(s)), sorted(expected))

        s = "(a)())()"
        expected = ["(a)()()", "(a())()"]
        self.assertEqual(sorted(sol.removeInvalidParentheses(s)), sorted(expected))

        s = ")("
        expected = [""]
        self.assertEqual(sorted(sol.removeInvalidParentheses(s)), sorted(expected))