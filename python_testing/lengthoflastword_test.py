import unittest

from leetcode.lengthoflastword.solution import Solution

class SolutionTest(unittest.TestCase):
    def testLengthOfLastWord(self):
        sol = Solution()
        s = "   fly me   to   the moon  "
        self.assertEqual(4, sol.lengthOfLastWord(s))

        s = "luffy is still joyboy"
        self.assertEqual(6, sol.lengthOfLastWord(s))