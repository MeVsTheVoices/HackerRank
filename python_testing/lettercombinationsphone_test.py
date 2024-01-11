import unittest
from leetcode.lettercombinationphone.solution import Solution

class TestSolution(unittest.TestCase):
    def testLetterCombinations(self):
        sol = Solution()
        self.assertEqual(sol.letterCombinations("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
        self.assertEqual(sol.letterCombinations("2"), ["a", "b", "c"])
        self.assertEqual(sol.letterCombinations(""), [])
        self.assertEqual(sol.letterCombinations("234"), ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"])
