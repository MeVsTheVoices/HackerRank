import unittest
from cs497.assignment5.shortestpathvisitingallnodes.solution import Solution

class TestSolution(unittest.TestCase):
    def testShortestPathLength(self):
        testCases = [
            {
                'graph': [[1,2,3],[0],[0],[0]],
                'want': 4,
            },
            {
                'graph': [[1],[0,2,4],[1,3,4],[2],[1,2]],
                'want': 4,
            },
        ]
        for tc in testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    Solution().shortestPathLength(tc['graph']),
                    tc['want'],
                )