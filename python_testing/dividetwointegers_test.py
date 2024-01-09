import unittest
from leetcode.dividetwointegers.solution import Solution

class TestSolution(unittest.TestCase):
    def testFindDivisible(self):
        sol = Solution()
        dividend = 10
        divisor = 3
        quotient = sol.divide(dividend, divisor)
        self.assertEqual(quotient, 3)

        dividend = 7
        divisor = -3
        quotient = sol.divide(dividend, divisor)
        self.assertEqual(quotient, -2)