import unittest
from cs497.final.besttimetobuyandsell import Solution

class TestSolution(unittest.TestCase):
    def testMaxProfit(self):
        # Input: prices = [7,1,5,3,6,4]
        # Output: 5
        # Input: prices = [7,6,4,3,1]
        # Output: 0
        solution = Solution()
        self.assertEqual(solution.maxProfit([7,1,5,3,6,4]), 5)
        self.assertEqual(solution.maxProfit([7,6,4,3,1]), 0)