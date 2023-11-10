import unittest
from cs497.assignment5.lexicographicalnumbers.solution import Solution

class TestSolution(unittest.TestCase):
    def testLexicalOrder(self):
        sol = Solution()
        self.assertEqual(sol.lexicalOrder(13), [1,10,11,12,13,2,3,4,5,6,7,8,9])
        self.assertEqual(sol.lexicalOrder(1), [1])
        self.assertEqual(sol.lexicalOrder(2), [1,2])
        