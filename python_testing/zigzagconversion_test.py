import unittest
# leetcode\zigzagconversion
from leetcode.zigzagconversion.solution import Solution

class TestSolution(unittest.TestCase):
    def testConvert(self):
        testCases = [
            {
                's': 'PAYPALISHIRING',
                'numRows': 3,
                'want': 'PAHNAPLSIIGYIR',
            },
            {
                's': 'PAYPALISHIRING',
                'numRows': 4,
                'want': 'PINALSIGYAHRPI',
            },
            {
                's': 'A',
                'numRows': 1,
                'want': 'A',
            },
        ]
        for tc in testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    Solution().convert(tc['s'], tc['numRows']), tc['want'])