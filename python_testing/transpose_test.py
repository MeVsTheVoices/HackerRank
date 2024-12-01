import unittest
from leetcode.transpose.solution import Solution

class TransposeTest(unittest.TestCase):
    def testTranspose(self):
        solution = Solution()
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(solution.transpose(matrix), [[1,4,7],[2,5,8],[3,6,9]])