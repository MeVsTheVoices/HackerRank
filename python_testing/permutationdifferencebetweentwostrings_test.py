import unittest
from leetcode.permutationdifferencebetweentwostrings.solution import Solution

class TestSolution(unittest.TestCase):
    def testFindPermutationDifference(self):
        sol = Solution()
        self.assertEqual(sol.findPermutationDifference("abc", "bac"), 2)
        self.assertEqual(sol.findPermutationDifference("abcde", "edbac"), 12)
        