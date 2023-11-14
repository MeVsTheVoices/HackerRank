import unittest
from cs497.assignment6.validpaths.solution import Solution

class TestSolution(unittest.TestCase):
    def testValidPath(self):
        sol = Solution()
        n = 3
        paths = [[0,1],[1,2],[2,0]]
        source = 0
        destination = 2
        expected = True
        actual = sol.validPath(n, paths, source, destination)
        self.assertEqual(expected, actual)

        n = 6
        paths = [[0,1],[0,2],[3,5],[5,4],[4,3]]
        source = 0
        destination = 5
        expected = False
        actual = sol.validPath(n, paths, source, destination)
        self.assertEqual(expected, actual)