import unittest
from cs497.assignment6.findallpaths.solution import Solution

class TestSolution(unittest.TestCase):
    def testAllPathsSourceTarget(self):
        sol = Solution()
        graph = [[1,2],[3],[3],[]]
        expected = [[0,1,3],[0,2,3]]
        actual = sol.allPathsSourceTarget(graph)
        self.assertEqual(len(expected), len(actual))
        for expect in expected:
            self.assertTrue(expect in actual)

        graph = [[4,3,1],[3,2,4],[3],[4],[]]
        expected = [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
        actual = sol.allPathsSourceTarget(graph)
        self.assertEqual(len(expected), len(actual))
        for expect in expected:
            self.assertTrue(expect in actual)
        