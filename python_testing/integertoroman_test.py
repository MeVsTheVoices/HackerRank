import unittest
from leetcode.integertoroman.solution import Solution

class TestSolution(unittest.TestCase):
    def testIntToRoman(self):
        sol = Solution()
        input = 3
        output = "III"
        self.assertEqual(sol.intToRoman(input), output)
        input = 58
        output = "LVIII"
        self.assertEqual(sol.intToRoman(input), output)
        input = 1994
        output = "MCMXCIV"
        self.assertEqual(sol.intToRoman(input), output)
