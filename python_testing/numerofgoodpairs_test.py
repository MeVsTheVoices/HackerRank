import unittest
from leetcode.numberofgoodpairs.solution import Solution

class TestSolution(unittest.TestCase):
    def testNumIdenticalPairs(self):
        sol = Solution()
        nums = [1,2,3,1,1,3]
        self.assertEqual(sol.numIdenticalPairs(nums), 4)

        nums = [1,1,1,1]
        self.assertEqual(sol.numIdenticalPairs(nums), 6)

        nums = [1,2,3]
        self.assertEqual(sol.numIdenticalPairs(nums), 0)

        