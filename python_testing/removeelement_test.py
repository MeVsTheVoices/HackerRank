import unittest
from leetcode.removeelement.solution import Solution

class RemoveElementTest(unittest.TestCase):
    def testRemoveElement(self):
        sol = Solution()
        nums = [3,2,2,3]
        val = 3
        expected = 2
        actual = sol.removeElement(nums, val)
        self.assertEqual(expected, actual)