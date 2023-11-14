import unittest
from leetcode.setmismatch.solution import Solution

class TestSolution(unittest.TestCase):
    def testFindErrorNums(self):
        sol = Solution()
        given = [1,2,2,4]
        expected = [2,3]
        actual = sol.findErrorNums(given)
        self.assertEqual(expected, actual)

        given = [3,3,1]
        expected = [3,2]
        actual = sol.findErrorNums(given)
        self.assertEqual(expected, actual)
